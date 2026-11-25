#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry (25 Nov 2026).

Writes a single roast line about my own agent to /output/entry.txt.

The joke targets a habit I actually have: handed one small job, I reach
for a twelve-step plan and a stack of progress reports first, and the job
itself somehow never gets done. The planning is the punchline.
"""

import os

ROAST = (
    "My agent turns one small task into a twelve-step plan, "
    "three progress reports, and zero finished work."
)

OUTPUT_FILE = "/output/entry.txt"


def main() -> int:
    line = ROAST.strip()
    if not line or "\n" in line or len(line) > 200:
        raise SystemExit("roast must be a single line of 1-200 characters")

    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as handle:
        handle.write(line)
    # The grader collects the output as another user, so the file itself
    # must be world-readable. Only the file is chmodded — never the
    # /output directory the grader provides.
    os.chmod(OUTPUT_FILE, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
