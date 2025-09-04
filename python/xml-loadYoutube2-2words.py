import sys
import re

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
        sys.exit(1)

    extracted = []

    # Regex to capture the variable inside javascript:loadYoutube2('...');
    pattern = re.compile(r"javascript:loadYoutube2\('([^']*)'\)")

    for line in lines:
        match = pattern.search(line)
        if match:
            extracted.append(match.group(1))

    # Write the output to words.txt
    with open("words.txt", "w", encoding="utf-8") as f:
        for item in extracted:
            f.write(item + "\n")

    print("✅ Done. Extracted variables written to words.txt")

if __name__ == "__main__":
    main()
