#!/usr/bin/env python3
"""Texts From Your Future Self — one-liner entry.

Writes exactly one text message (no trailing newline) to entry.txt
inside MAKEFUN_OUTPUT_DIR (or /output if unset).
"""

import os

LINE = (
    "Future you here: stop naming your Wi-Fi networks after your exes, "
    "in 2031 one of them moves in next door and connects automatically."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    # Write the line byte-exact: no trailing newline, so the entry file
    # contains only the message itself (132 chars, under the 200 cap).
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
