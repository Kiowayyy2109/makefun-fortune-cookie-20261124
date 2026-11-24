"""Fortune Cookie Wisdom for Developers.

Writes one original line of fortune-cookie wisdom for a software
developer to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line must be at most 120 characters, as required by the competition.
"""

import os

LINE = "The bug you fear most is already fixed in the branch you forgot to merge."

MAX_CHARS = 120


def main() -> None:
    if len(LINE) > MAX_CHARS:
        raise ValueError(
            "entry line is %d characters, over the %d-character limit"
            % (len(LINE), MAX_CHARS)
        )
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(output_dir, "entry.txt")
    os.makedirs(output_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print("wrote %s (%d characters)" % (path, len(LINE)))


if __name__ == "__main__":
    main()
