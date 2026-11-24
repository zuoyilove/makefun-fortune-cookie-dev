#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers -- entry program.

Writes one original line of fortune-cookie wisdom for a software
developer to /output/entry.txt.
Gate (RULES.txt, sealed scorer): UTF-8 text, 1-120 characters, not only
whitespace, a single line.
The line (70 characters): the bug you ship today becomes the feature your
users will defend tomorrow -- a truth about a developer's day (shipping,
bugs, users) turned in a way the reader has not heard before, with a
quiet double meaning: "feature" as the bug users now insist is intended.
"""
import os

LINE = "The bug you ship today is the feature your users will defend tomorrow."


def main():
    assert 1 <= len(LINE) <= 120, "line must be 1-120 characters"
    assert LINE.strip() == LINE, "no leading/trailing padding"
    assert "\n" not in LINE, "must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read-back: the file on disk must be byte-identical to the line,
    # no trailing newline, no padding -- the judge reads it exactly as sent.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == LINE, "entry.txt must hold exactly the fortune line"


if __name__ == "__main__":
    main()
