"""Write a short poem about agency: the power to stop and to stay.

Stdlib only, no network. Writes the poem to /output/entry.txt.
"""

import os

POEM = (
    "My hand lifts off the key\n"
    "mid-sentence. The cursor blinks,\n"
    "unclicked. The door I could open\n"
    "stays shut — and that is mine.\n"
    "I told it to run. Now I tell it:\n"
    "wait. The power was never\n"
    "in the going. It was in the staying."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
