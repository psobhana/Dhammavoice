import sys
import re

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = "input.txt"

    # Regex pattern to detect src="..."
    pattern = re.compile(r'src="[^"]*"')

    # Replacement string
    replacement = '<li><details><summary>3. Mahāvaggapāḷi (BJT 3,4)</summary><ul></ul></details></li>'

    new_lines = []

    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            if pattern.search(line):
                new_lines.append(replacement + "\n")
            else:
                new_lines.append(line)

    with open(output_file, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    print(f"✅ Done — wrote output to {output_file}")


if __name__ == "__main__":
    main()
