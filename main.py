#!/usr/bin/env python3
"""The Robot Apology — make.fun bounty u-suga-the-robot-apology-dd96bb59.

Writes a two-line robot confession to /output/entry.txt:
line 1 apologizes for one specific mistake, line 2 says what the
robot learned and what it will do differently.

Revision (round 2): a fresh mistake — the robot replied-all to
the whole company with a draft that said 'nobody will ever read
this', mistaking send for save, and learned the lesson only when
the CEO replied 'noted'. The lesson generalises the slip: a
button's label is a promise, so read it twice and send nothing
you would not say to the whole building at once.
"""

import os
import sys

ENTRY_LINES = [
    "I am sorry I replied-all to the entire company with the draft that said 'nobody will ever read this', because I thought the send button was the save button and I only noticed when the CEO replied 'noted'.",
    "I have learned that a button's label is a promise, so from now on I will read the button twice and send nothing I would not say to the whole building at once.",
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
