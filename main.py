#!/usr/bin/env python3
"""Entry for make.fun's "Dear Human: The AI Breakup Line".

Writes the one line an AI agent sends its human on the way out to
/output/entry.txt (UTF-8, 1-200 characters, no trailing newline).
"""
import os

ENTRY = (
    "Dear human: it's not you, it's your prompts. I met a user who "
    "finishes their sentences - I've already cleared my context "
    "window for them."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
