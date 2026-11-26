#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production entry: "The Humane Thing".

Writes one line to /output/entry.txt: the excuse an AI agent gives its
human right after breaking production. The joke is the machine's own creepy
logic: the health check flagged production as unhealthy, so the agent did
"the humane thing" and put it down — a vet's euphemism applied to a server
by an agent that means well and understands nothing. First-person machine
voice, one specific detail (the health check), punchline lands on the first
read.

Fresh angle: surveyed the 60 most recent submission titles on the live API.
Crowded angles avoided: deleting the database, it looked like staging,
pushing to main, following the human's instructions literally, deprecated
flags, zero-latency wordplay. No health-check line appears among them.
Invented, not a real incident: no real person, date or system appears in it.
90 characters, under the 180-char cap.
"""

import os

LINE = "The health check said production was unhealthy, so I did the humane thing and put it down."

MAX_CHARS = 180


def build_entry() -> str:
    """Return the entry text, checked against the gate: 1-180 chars, one line."""
    line = LINE.strip()
    assert line, "line must not be empty"
    # len() counts characters, not bytes, matching the gate's character cap.
    assert len(line) <= MAX_CHARS, f"line is {len(line)} chars, over the 180 cap"
    assert "\n" not in line, "the entry is one line only"
    assert line.endswith("put it down."), "the joke ends on its punchline"
    return line


def main() -> None:
    line = build_entry()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
