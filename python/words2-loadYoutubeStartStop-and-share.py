#!/usr/bin/env python3
import sys
import re

def parse_word_line(line):
    """Parse a line from words.txt into (video_id, start, stop_or_none)."""
    parts = [p.strip() for p in line.split(",")]
    video_id = parts[0]
    if len(parts) == 3:   # id, start, stop
        return video_id, parts[1], parts[2]
    elif len(parts) == 2: # id, single time
        return video_id, parts[1], None
    else:
        raise ValueError(f"Invalid line in words.txt: {line}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python replace_ids.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    # Load replacements
    try:
        with open("words.txt", "r", encoding="utf-8") as f:
            replacements = [parse_word_line(line.strip()) for line in f if line.strip()]
    except FileNotFoundError:
        print("Error: words.txt not found.")
        sys.exit(1)

    if not replacements:
        print("Error: words.txt is empty.")
        sys.exit(1)

    last_replacement = replacements[-1]     # for Start()
    stop_replacements = replacements[:-1]   # for StartStop()

    # Load input file
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
        sys.exit(1)

    out_lines = []
    replacement_index = 0

    for line in lines:
        new_line = line

        # Handle StartStop replacements
        if replacement_index < len(stop_replacements):
            video_id, start, stop = stop_replacements[replacement_index]

            def repl_stop(m):
                func = m.group(1)
                return f"{func}('{video_id}', {start}, {stop})"

            new_line = re.sub(r"(loadYoutubeStartStop|sharePageSrartStop)\([^)]*\)", repl_stop, new_line)
            if new_line != line:
                replacement_index += 1

        # Handle Start replacements
        video_id, time_val, stop = last_replacement
        def repl_start(m):
            func = m.group(1)
            return f"{func}('{video_id}', {time_val})"

        new_line = re.sub(r"(loadYoutubeStart|sharePageSrart)\([^)]*\)", repl_start, new_line)

        out_lines.append(new_line)

    # Save output
    with open("output2.txt", "w", encoding="utf-8") as f:
        f.writelines(out_lines)

    print("Done — wrote output2.txt")

if __name__ == "__main__":
    main()
