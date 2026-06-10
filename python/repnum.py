#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} input.html")
    sys.exit(1)

input_file = sys.argv[1]
numbers_file = "numbers.txt"
output_file = "output.html"

# Load replacements from numbers.txt
replacements = {}

with open(numbers_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or "=" not in line:
            continue

        key, value = line.split("=", 1)
        replacements[key.strip()] = value.strip()

# Sort keys by length descending so "min" is replaced before "m", etc.
replacement_items = sorted(
    replacements.items(),
    key=lambda x: len(x[0]),
    reverse=True
)


def convert_text(text):
    """Apply all replacements to a text string."""
    for old, new in replacement_items:
        text = text.replace(old, new)
    return text


# Regex for <summary>text</summary>
summary_pattern = re.compile(
    r'(<summary>)(.*?)(</summary>)',
    re.IGNORECASE
)

# Regex for the first button on a line
first_button_pattern = re.compile(
    r'(<button\b[^>]*>)(.*?)(</button>)',
    re.IGNORECASE
)

with open(input_file, "r", encoding="utf-8") as fin, \
     open(output_file, "w", encoding="utf-8") as fout:

    for line in fin:

        # Replace text inside every <summary>...</summary>
        line = summary_pattern.sub(
            lambda m: m.group(1) + convert_text(m.group(2)) + m.group(3),
            line
        )

        # Replace text inside ONLY the first <button>...</button>
        line = first_button_pattern.sub(
            lambda m: m.group(1) + convert_text(m.group(2)) + m.group(3),
            line,
            count=1
        )

        fout.write(line)

print(f"Output written to {output_file}")