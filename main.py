#!/usr/bin/env python3
"""Worst Fix Ever entry: write one commit message to /output/entry.txt.

The entry is a single commit message line (42 characters) for a bug fix
that made everything worse: the login crash was "fixed" by removing
login entirely.
"""

import os

ENTRY = "fix: stop crash on login by removing login"  # 42 chars, one line


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
