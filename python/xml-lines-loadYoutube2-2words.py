import sys
import re

def main():
    # Check if file argument is given
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = "words.txt"

    # Regex pattern for javascript:loadYoutube2('something');
    pattern = re.compile(r"javascript:loadYoutube2\('.*?'\);")

    results = []

    # Open file as utf-8
    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            match = pattern.search(line)
            if match:
                results.append(match.group(0))

    # Write results to words.txt
    with open(output_file, "w", encoding="utf-8") as f:
        for item in results:
            f.write(item + "\n")

    print(f"Done — extracted {len(results)} lines to {output_file}")


if __name__ == "__main__":
    main()
