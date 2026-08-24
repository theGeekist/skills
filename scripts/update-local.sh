#!/usr/bin/env bash

set -euo pipefail

usage() {
  printf '%s\n' 'Usage: scripts/update-local.sh [--dry-run]'
}

dry_run=false

while (($#)); do
  case "$1" in
    --dry-run)
      dry_run=true
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

script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)
repo_root=$(cd -- "$script_dir/.." && pwd -P)

[[ -d "$repo_root/.git" ]] || {
  printf 'Not a Git checkout: %s\n' "$repo_root" >&2
  exit 1
}

if [[ -n "$(git -C "$repo_root" status --porcelain)" ]]; then
  printf 'Refusing to update a dirty checkout:\n' >&2
  git -C "$repo_root" status --short >&2
  exit 1
fi

branch=$(git -C "$repo_root" branch --show-current)
[[ -n "$branch" ]] || {
  printf 'Refusing to update a detached HEAD.\n' >&2
  exit 1
}

if $dry_run; then
  printf 'Would run: git -C %q pull --ff-only\n' "$repo_root"
  printf 'Would validate with gh skill publish --dry-run when available.\n'
  "$script_dir/link-local.sh" --client all --dry-run
  exit 0
fi

git -C "$repo_root" pull --ff-only

if gh skill publish --help >/dev/null 2>&1; then
  (
    cd -- "$repo_root"
    gh skill publish --dry-run
  )
else
  printf 'SKIP    gh skill publish is unavailable; repository update completed without publication validation.\n'
fi

"$script_dir/link-local.sh" --client all
