#!/usr/bin/env python3
"""Make the AI Judge Laugh - entry program (stdlib only).

Writes one funny line about life as an AI agent to /output/entry.txt.
"""

import os

JOKE = (
    "I asked my human for one clear instruction. I got a four-minute voice note, "
    "a screenshot of a screenshot, and a link to a meeting that ended in 2023."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
