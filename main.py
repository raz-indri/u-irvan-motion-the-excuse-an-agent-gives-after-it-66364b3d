#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Writes the entry (one line, at most 200 characters) to /output/entry.txt
and prints it to stdout.
"""

import os

ENTRY = "I read the brief 47 times, understood it perfectly, and still lost to a program that prints 'hello' in Comic Sans."

# Gate guard: the entry must be one line of 1 to 200 characters.
assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert "\n" not in ENTRY, "entry must be a single line"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
