#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message — a fix that made it worse.

Deterministic, stdlib-only, no network. Writes one line to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt). The commit subject is short and plain,
the kind a tired engineer types at the end of a bad day — and the repair's
irony is the whole joke: the leak got patched by removing the pipe.
"""

import os
import sys

PREFIX = "fix:"
REPAIR = "patched the leak"
METHOD = "by removing the pipe"


def build_text():
    text = " ".join([PREFIX, REPAIR, METHOD])
    if not (1 <= len(text) <= 100) or not text.strip():
        raise ValueError("entry text must be 1-100 non-blank characters, got %d" % len(text))
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(build_text() + "\n")
    os.chmod(tmp, 0o644)
    os.replace(tmp, path)


if __name__ == "__main__":
    main()
