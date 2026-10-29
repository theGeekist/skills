#!/usr/bin/env python3
"""Record Linux file-access events for one isolated skill-selection experiment.

Access is evidence that a file was read by a process, not proof that every byte
entered a model context. No document content is recorded. Stop with --stop-file.
"""

import argparse
import ctypes
import json
import os
from pathlib import Path
import select
import struct
import time


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--stop-file", type=Path, required=True)
    parser.add_argument("--seconds", type=int, default=900)
    args = parser.parse_args()
    root = args.root.resolve()
    libc = ctypes.CDLL(None, use_errno=True)
    descriptor = libc.inotify_init1(os.O_NONBLOCK | os.O_CLOEXEC)
    if descriptor < 0:
        raise OSError(ctypes.get_errno(), "inotify_init1 failed")
    names = {}
    for path in root.rglob("*"):
        if path.is_file():
            watch = libc.inotify_add_watch(descriptor, os.fsencode(path), 0x1)
            if watch < 0:
                raise OSError(ctypes.get_errno(), "inotify_add_watch failed")
            names[watch] = str(path.relative_to(root))
    started = time.monotonic()
    started_unix = time.time()
    events = []
    try:
        while not args.stop_file.exists() and time.monotonic() - started < args.seconds:
            if not select.select([descriptor], [], [], 0.25)[0]:
                continue
            try:
                data = os.read(descriptor, 65536)
            except BlockingIOError:
                continue
            offset = 0
            while offset < len(data):
                watch, mask, cookie, length = struct.unpack_from("iIII", data, offset)
                offset += 16 + length
                if mask & 0x1 and watch in names:
                    events.append({"path": names[watch], "elapsed_seconds": round(time.monotonic() - started, 3)})
    finally:
        os.close(descriptor)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps({"kind": "linux-inotify-file-access", "root": str(root), "started_monotonic": started, "started_unix": started_unix,
            "limitation": "File access does not establish model context consumption or native runtime activation.",
            "events": events}, indent=2) + "\n")


if __name__ == "__main__":
    main()
