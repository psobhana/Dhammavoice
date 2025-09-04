import sys
import re

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    # Read replacement lines from words.txt (keep them unchanged)
    try:
        with open("words.txt", "r", encoding="utf-8") as f:
            replacements = [line.rstrip("\n") for line in f]
    except FileNotFoundError:
        print("Error: words.txt not found.")
        sys.exit(1)

    # Read the input file
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    output_lines = []
    replacement_index = 0

    for line in lines:
        if replacement_index < len(replacements):
            replacement_text = replacements[replacement_index]

            # Replace with a function so regex won’t interpret digits as group references
            def replacer(match, replacement=replacement_text):
                return match.group(1) + replacement + match.group(3)

            new_line = re.sub(
                r'(<button[^>]*>)(.*?)(</button>)',
                replacer,
                line,
                count=1
            )
            output_lines.append(new_line)
            replacement_index += 1
        else:
            output_lines.append(line)

    # Always write to output.txt
    with open("output.txt", "w", encoding="utf-8") as f:
        f.writelines(output_lines)

    print("Done. Output written to output.txt")

if __name__ == "__main__":
    main()
