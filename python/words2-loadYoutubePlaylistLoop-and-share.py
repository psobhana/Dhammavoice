#!/usr/bin/env python3
import sys
import re

def main():
    if len(sys.argv) < 2:
        print("Usage: python replace_ids.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    # Read replacements from words.txt
    try:
        with open("words.txt", "r", encoding="utf-8") as f:
            replacements = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("Error: words.txt not found.")
        sys.exit(1)

    # Read input file
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
        sys.exit(1)

    out_lines = []
    replacement_index = 0

    # regex for the playlist loop call
    loop_pattern = re.compile(
        r"(loadYoutubePlaylistLoop\s*\(\s*['\"])([^'\"]+)(['\"]\s*,\s*)(true|false)(\s*\)\s*;)"
    )
    # regex for the share call
    share_pattern = re.compile(
        r"(sharePagePlaylist\s*\(\s*['\"])([^'\"]+)(['\"]\s*\))"
    )

    for line in lines:
        if replacement_index < len(replacements):
            parts = [p.strip() for p in replacements[replacement_index].split(",", 1)]
            playlist_id = parts[0]
            flag = parts[1] if len(parts) > 1 else "true"

            # Replace only inside the function calls
            line = loop_pattern.sub(
                lambda m: m.group(1) + playlist_id + m.group(3) + flag + m.group(5),
                line,
            )
            line = share_pattern.sub(
                lambda m: m.group(1) + playlist_id + m.group(3),
                line,
            )

            replacement_index += 1

        out_lines.append(line)

    # Write output
    with open("output2.txt", "w", encoding="utf-8") as f:
        f.writelines(out_lines)

    print(f"Done — wrote output2.txt")
    print(f"Replacements consumed from words.txt: {replacement_index}")
    if replacement_index < len(replacements):
        print(f"{len(replacements) - replacement_index} lines in words.txt unused.")

if __name__ == "__main__":
    main()
