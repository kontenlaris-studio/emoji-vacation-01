#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — writes exactly one emoji to /output/entry.txt.

The emoji: a moai. Not just any beach — the whole bucket-list story
in one stone face: the long flight to the most remote island on
Earth, the statues at sunrise, the trip you describe in one breath.
"""
import os

EMOJI = "🗿"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EMOJI + "\n")
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
