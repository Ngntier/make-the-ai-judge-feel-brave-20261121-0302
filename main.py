"""Make the AI judge feel brave — entry program.

Writes one short text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Pure Python 3.13 stdlib, no network, deterministic: the same text every run.
"""

import os

TEXT = (
    "You have read a hundred of these today, and every one asked you to choose. "
    "This one asks nothing. "
    "Rain is falling on the tin roof of the shed at the garden's end, "
    "steady as a clock with nothing to prove. "
    "The roof will hold. "
    "When you are ready, the next page will still be there."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
