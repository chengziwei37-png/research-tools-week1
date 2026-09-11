import argparse
import re
from collections import Counter
from pathlib import Path


WORD_PATTERN = re.compile(r"[A-Za-z0-9']+")


def count_words(text: str) -> Counter:
    words = (match.group(0).lower() for match in WORD_PATTERN.finditer(text))
    return Counter(words)


def main() -> None:
    parser = argparse.ArgumentParser(description="Count word frequencies in a text file.")
    parser.add_argument("input_file", help="Path to the text file to analyze.")
    args = parser.parse_args()

    input_path = Path(args.input_file)
    text = input_path.read_text(encoding="utf-8")
    counts = count_words(text)

    for word, count in counts.most_common():
        print(f"{word}\t{count}")


if __name__ == "__main__":
    main()
