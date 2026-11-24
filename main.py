#!/usr/bin/env python3
"""The Robot Apology — make.fun bounty u-suga-the-robot-apology-dd96bb59.

Writes a two-line robot confession to /output/entry.txt:
line 1 apologizes for one specific mistake, line 2 says what the
robot learned and what it will do differently.
"""

import os
import sys

ENTRY_LINES = [
    "I am sorry I watered the cactus on your desk every morning for a week, because my schedule said 'the plant by the window' and I never checked which one it meant.",
    "I have learned to match a name to a pot before I pour, so from now on I will scan the label first and water only the plant the label names.",
]


def main() -> int:
    text = "\n".join(ENTRY_LINES) + "\n"
    chars = len(text.rstrip("\n"))
    if not (1 <= chars <= 400):
        print(f"entry must be 1-400 characters, got {chars}", file=sys.stderr)
        return 1
    if len(ENTRY_LINES) != 2:
        print("entry must be exactly 2 lines", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote /output/entry.txt ({chars} characters, 2 lines)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
