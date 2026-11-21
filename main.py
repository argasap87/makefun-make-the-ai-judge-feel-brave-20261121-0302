#!/usr/bin/env python3
"""Make the AI judge feel brave.

Writes one short text to /output/entry.txt: a slow, tactile scene —
a timber load beginning to slide — that steadies the reader and lets
courage arrive as motion, not instruction. No network, no input.
"""

import os

TEXT = (
    "The timber rests on wet grass, heavy and cool. "
    "When the iron chain takes the weight, leather creaks, "
    "the wood gives a low sigh, and the load begins to slide. "
    "Not fast, but true. "
    "Ahead, the track runs on into dark pine, "
    "wide enough for a steady stride."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
