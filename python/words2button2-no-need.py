import sys
import re

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    # Read replacement lines from word.txt (exactly as they are)
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

            # Safe replacement: use a function instead of raw string
            def replace_func(match):
                return match.group(1) + replacement_text + match.group(3)

            new_line = re.sub(
                r'(<button[^>]*>)(.*?)(</button>)',
                replace_func,
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

    print("✅ Done. Output written to output.txt")

if __name__ == "__main__":
    main()
