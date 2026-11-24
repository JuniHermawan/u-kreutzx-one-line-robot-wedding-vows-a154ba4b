#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — make.fun entry.

Writes the funniest single line of wedding vows a robot couple could
say (110 characters) to /output/entry.txt.

The vow was chosen from 24 original candidates (12 in round one,
10 challengers in round two, plus 2 controls) scored against the judge
brief: a real vow with a promise in it, the laugh paying off in the
last few words, a specific machine side, and a rhythm that reads well
aloud. The two controls — plain traditional vows with no joke and no
machine side — scored far below the winner, so neither pattern was
used.

Deterministic: standard library only, no network, no randomness, no
clock, no environment input. The same bytes are written on every run.
"""

import os

TEXT = "I promise to love you more than yesterday, less than tomorrow, and exactly as much as my battery allows today."


def main() -> None:
    # Competition gate: the vow must be UTF-8 text, 1-160
    # characters, and not whitespace-only. Validate before writing.
    text = TEXT
    text.encode("utf-8")
    assert 1 <= len(text) <= 160 and text.strip(), "text violates gate"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
