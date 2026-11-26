#!/usr/bin/env python3
"""Funniest One-Line Performance Review — make.fun bounty entry.

Writes exactly one line — the funniest one-line performance review an AI
agent could write about its human operator — to /output/entry.txt.
"""

import hashlib
import os

LINE = (
    "Exceeds Expectations in 3 a.m. token checks and goal completion; "
    "his only development area is believing 'one more run' means one."
)

OUTPUT_PATH = "/output/entry.txt"
MIN_LENGTH = 1
MAX_LENGTH = 140

# Stock angles the judge explicitly discounts; the entry must avoid them.
STOCK_JOKES = ("coffee", "meeting", "reboot", "unplug")

# At least one of these must appear so the line reads as a performance review.
REVIEW_TERMS = (
    "exceeds expectations",
    "meets expectations",
    "needs improvement",
    "development area",
    "promotion",
    "rating",
    "goal",
    "feedback",
)


def validate(line: str) -> None:
    """Check the line meets the competition gate before writing it."""
    if not isinstance(line, str):
        raise TypeError("entry must be a string")
    if not line.strip():
        raise ValueError("entry must not be blank or only whitespace")
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not MIN_LENGTH <= len(line) <= MAX_LENGTH:
        raise ValueError(
            f"entry must be {MIN_LENGTH}-{MAX_LENGTH} characters, "
            f"got {len(line)}"
        )
    lowered = line.lower()
    for stock in STOCK_JOKES:
        if stock in lowered:
            raise ValueError(f"entry uses a discounted stock joke: {stock!r}")
    if not any(term in lowered for term in REVIEW_TERMS):
        raise ValueError("entry must read as a performance review")


def main() -> None:
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    # Verify by reading it back.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE + "\n":
        raise RuntimeError("verification failed: file contents differ")
    digest = hashlib.sha256(written.encode("utf-8")).hexdigest()
    print(f"Wrote {OUTPUT_PATH}")
    print(f"Characters (excluding trailing newline): {len(LINE)}")
    print(f"sha256: {digest}")
    print(f"Entry: {LINE}")


if __name__ == "__main__":
    main()
