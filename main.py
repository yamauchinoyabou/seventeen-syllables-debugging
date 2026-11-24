"""Write a debugging haiku to /output/entry.txt.

Syllable counts: 5-7-5
    Three a.m. cursor               (5)
    on the line I swore was fine—   (7)
    my name in git blame            (5)

The twist: a late-night hunt for the culprit behind a bug ends with
git blame pointing back at the person debugging. The line "I swore
was fine" was the debugger's own.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

HAIKU_LINES = [
    "Three a.m. cursor",
    "on the line I swore was fine—",
    "my name in git blame",
]


def build_content(lines: list[str]) -> bytes:
    """Join the lines with LF, add a trailing newline, and encode as UTF-8."""
    return ("\n".join(lines) + "\n").encode("utf-8")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(build_content(HAIKU_LINES))


if __name__ == "__main__":
    main()
