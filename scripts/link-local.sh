#!/usr/bin/env bash

set -euo pipefail

usage() {
  printf '%s\n' \
    'Usage: scripts/link-local.sh [--client all|codex|claude|gemini|antigravity|antigravity-cli] [--dry-run] [--adopt]' \
    '' \
    'Links every repository skill into the selected clients.' \
    '--adopt moves conflicting destinations to timestamped backups before linking.'
}

client='all'
dry_run=false
adopt=false

while (($#)); do
  case "$1" in
    --client)
      [[ $# -ge 2 ]] || { usage >&2; exit 2; }
      client="$2"
      shift 2
      ;;
    --dry-run)
      dry_run=true
      shift
      ;;
    --adopt)
      adopt=true
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      printf 'Unknown argument: %s\n' "$1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

case "$client" in
  all|codex|claude|gemini|antigravity|antigravity-cli) ;;
  *)
    printf 'Unsupported client: %s\n' "$client" >&2
    exit 2
    ;;
esac

script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)
repo_root=$(cd -- "$script_dir/.." && pwd -P)
skill_root="$repo_root/plugins/geekist-architecture-skills/skills"
user_home_dir=${HOME:?HOME is required}
backup_stamp=$(date -u '+%Y%m%dT%H%M%SZ')

[[ -d "$skill_root" ]] || {
  printf 'Skill root not found: %s\n' "$skill_root" >&2
  exit 1
}

run() {
  if $dry_run; then
    printf 'Would run:'
    printf ' %q' "$@"
    printf '\n'
  else
    "$@"
  fi
}

resolved_path() {
  local path=$1
  if command -v realpath >/dev/null 2>&1; then
    realpath "$path" 2>/dev/null || true
  else
    python3 -c 'import os, sys; print(os.path.realpath(sys.argv[1]))' "$path" 2>/dev/null || true
  fi
}

link_skill() {
  local source=$1
  local destination_root=$2
  local name destination resolved backup

  name=$(basename -- "$source")
  destination="$destination_root/$name"

  if [[ -e "$destination" || -L "$destination" ]]; then
    resolved=$(resolved_path "$destination")
    if [[ "$resolved" == "$source" ]]; then
      printf 'OK      %s -> %s\n' "$destination" "$source"
      return
    fi

    if ! $adopt; then
      printf 'CONFLICT %s\n' "$destination" >&2
      printf '         resolves to: %s\n' "${resolved:-unresolved}" >&2
      printf '         expected:    %s\n' "$source" >&2
      printf 'Re-run with --adopt to move the conflict to a timestamped backup.\n' >&2
      return 1
    fi

    backup="${destination}.backup-${backup_stamp}"
    [[ ! -e "$backup" && ! -L "$backup" ]] || {
      printf 'Backup already exists: %s\n' "$backup" >&2
      return 1
    }
    run mv "$destination" "$backup"
    printf 'BACKUP  %s\n' "$backup"
  fi

  run mkdir -p "$destination_root"
  run ln -s "$source" "$destination"
  printf 'LINK    %s -> %s\n' "$destination" "$source"
}

link_root() {
  local destination_root=$1
  local source
  while IFS= read -r source; do
    link_skill "$source" "$destination_root"
  done < <(find "$skill_root" -mindepth 2 -maxdepth 2 -type f -name SKILL.md -exec dirname '{}' \; | sort)
}

case "$client" in
  all)
    link_root "$user_home_dir/.agents/skills"
    link_root "$user_home_dir/.claude/skills"
    if command -v antigravity >/dev/null 2>&1 || [[ -d "$user_home_dir/.gemini/antigravity-cli" ]]; then
      link_root "$user_home_dir/.gemini/antigravity-cli/skills"
    else
      printf 'SKIP    Antigravity CLI is not installed; desktop Antigravity uses ~/.agents/skills.\n'
    fi
    ;;
  codex|gemini|antigravity)
    link_root "$user_home_dir/.agents/skills"
    ;;
  claude)
    link_root "$user_home_dir/.claude/skills"
    ;;
  antigravity-cli)
    link_root "$user_home_dir/.gemini/antigravity-cli/skills"
    ;;
esac
