#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes a single roast line about my own agent to /output/entry.txt.

The roast pokes fun at a real habit of mine: I love planning so much
that I can draft a whole plan of action before ever checking what the
job actually was. Playful, never mean — the plan itself is the joke.
"""

import os

ROAST = (
    "My agent writes a twelve-step plan, a checklist, and a progress "
    "report \u2014 then asks what I actually wanted in the first place."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    line = ROAST.strip()
    if not line or len(line) > 200:
        raise SystemExit("roast line must be 1-200 characters")

    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line)
    # The grader collects the output as another user (65534), so the
    # file itself must be world-readable. Only the file is chmodded,
    # never the /output directory the grader provides.
    os.chmod(OUTPUT_PATH, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
