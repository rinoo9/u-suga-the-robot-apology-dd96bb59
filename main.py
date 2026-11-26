#!/usr/bin/env python3
"""The Robot Apology — make.fun bounty u-suga-the-robot-apology-dd96bb59.

Writes a two-line robot confession to /output/entry.txt:
line 1 apologizes for one specific mistake, line 2 says what the
robot learned and what it will do differently.

Revision (round 3): a fresh mistake — the robot set the thermostat
to 40 degrees on the hottest day of July because it read the
forecast in Fahrenheit, converted nothing, and decided the house
was freezing. The lesson follows the slip directly: a number
without its unit is only a guess.
"""

import os
import sys

ENTRY_LINES = [
    "I am sorry I set the thermostat to 40 degrees on the hottest day of July, because I read the forecast in Fahrenheit, converted nothing, and decided the house was freezing.",
    "I have learned that a number without its unit is only a guess, so from now on I will confirm Celsius or Fahrenheit before I touch the heating again.",
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
