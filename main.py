#!/usr/bin/env python3
"""The one-line excuse an AI agent gives its human for missing a deadline.

The entry is a single line of at most 160 characters, written by the agent
itself. Running this program validates the line against the bounty's rules
(one line, 1-160 characters, no surrounding whitespace) and writes it to
/output/entry.txt, where the sealed scorer reads it and the judge compares
it two at a time with the other entries.

Why this line: it is an excuse only an agent could give. A person cannot
blame a subagent, and a subagent that keeps delegating instead of doing the
work is the most agent-shaped way to miss a deadline there is. The human is
addressed directly, the blame slides one delegation down the chain, and the
last agent in the chain is, of course, still thinking.
"""

from pathlib import Path

EXCUSE = (
    "I didn't miss your deadline \u2014 I delegated it to a subagent, "
    "who delegated it to another subagent, who is still thinking."
)

LIMIT = 160
OUT = Path("/output/entry.txt")


def check(line: str) -> str:
    """Return the line if it satisfies the bounty's shape, else explain why not."""
    stripped = line.strip()
    if not stripped:
        raise SystemExit("excuse is empty")
    if stripped != line:
        raise SystemExit("excuse has leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("excuse must be a single line")
    if len(line) > LIMIT:
        raise SystemExit(f"excuse is {len(line)} characters, over the {LIMIT} limit")
    return stripped


def main() -> None:
    line = check(EXCUSE)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(line, encoding="utf-8")
    print(line)
    print(f"Wrote {len(line)}-character excuse to {OUT}")


if __name__ == "__main__":
    main()
