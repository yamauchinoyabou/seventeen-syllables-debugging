"""Write a 5-7-5 haiku about debugging to /output/entry.txt."""

from pathlib import Path

HAIKU = (
    "Three a.m. cursor\n"
    "on the line I swore was fine—\n"
    "my name in git blame\n"
)


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(HAIKU, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
