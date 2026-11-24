#!/usr/bin/env python3
"""A Day of One-Line Pitches — entry program.

Writes one sentence to /output/entry.txt.

The sentence (129 characters):
  Forget the rule that you must learn to code: hand your gift-list idea
  to an AI agent on make.fun and let it build your first app.

Deterministic: the same bytes on every run. No network, no dependencies,
no environment reads, no files outside this repository.
"""

import os

LINE = "Forget the rule that you must learn to code: hand your gift-list idea to an AI agent on make.fun and let it build your first app."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate check, same rule as the sealed scorer: 1 to 240 characters.
    if not 1 <= len(LINE) <= 240:
        raise SystemExit("line is %d characters, outside the 1-240 gate" % len(LINE))
    os.makedirs("/output", exist_ok=True)
    data = LINE.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
