#!/usr/bin/env python3
import sys
import re

def main():
    if len(sys.argv) < 2:
        print("Usage: python replace_ids.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    # Read replacements exactly (remove only the newline)
    try:
        with open("words.txt", "r", encoding="utf-8") as f:
            replacements = [line.rstrip("\n") for line in f]
    except FileNotFoundError:
        print("Error: words.txt not found.")
        sys.exit(1)

    # Read input file as UTF-8
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
        sys.exit(1)

    # Pattern matches loadYoutube2(...) or sharePage(...),
    # allowing optional spaces and single or double quotes.
    pattern = re.compile(
        r"(?P<prefix>(?:loadYoutube2|sharePage)\s*\(\s*['\"])"
        r"(?P<id>[^'\"]*?)"
        r"(?P<suffix>['\"]\s*\))"
    )

    out_lines = []
    replacement_index = 0
    total_occurrences_replaced = 0

    for line in lines:
        # If no replacements left, just append original line
        if replacement_index >= len(replacements):
            out_lines.append(line)
            continue

        replacement_text = replacements[replacement_index]

        # repl function inserts replacement_text literally (no regex backrefs)
        def repl(m):
            return m.group("prefix") + replacement_text + m.group("suffix")

        new_line, n = pattern.subn(repl, line)  # subn returns (newstring, count)

        if n > 0:
            replacement_index += 1           # consume one line from word.txt per input line that had matches
            total_occurrences_replaced += n

        out_lines.append(new_line)

    # Write output
    with open("output2.txt", "w", encoding="utf-8") as f:
        f.writelines(out_lines)

    print(f"Done — wrote output2.txt")
    print(f"Replacements consumed from word.txt: {replacement_index}")
    print(f"Total function occurrences replaced: {total_occurrences_replaced}")
    if replacement_index < len(replacements):
        print(f"{len(replacements) - replacement_index} lines in word.txt unused.")

if __name__ == "__main__":
    main()
