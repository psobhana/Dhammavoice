#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re


def load_replacements(filename):
    replacements = {}

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or "=" not in line:
                continue

            key, value = line.split("=", 1)
            replacements[key.strip()] = value.strip()

    # Replace longer keys first (e.g. "min" before "m")
    return sorted(replacements.items(), key=lambda x: len(x[0]), reverse=True)


def replace_text(text, replacements):
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def replace_first_button(line, replacements):
    pattern = re.compile(r"(<button\b[^>]*>)(.*?)(</button>)", re.IGNORECASE)

    match = pattern.search(line)
    if not match:
        return line

    original_text = match.group(2)
    new_text = replace_text(original_text, replacements)

    return (
        line[:match.start(2)]
        + new_text
        + line[match.end(2):]
    )


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} input.html")
        sys.exit(1)

    input_file = sys.argv[1]
    replacements = load_replacements("numbers.txt")

    with open(input_file, "r", encoding="utf-8") as infile, \
         open("output.html", "w", encoding="utf-8") as outfile:

        for line in infile:
            outfile.write(replace_first_button(line, replacements))

    print("Created output.html")


if __name__ == "__main__":
    main()