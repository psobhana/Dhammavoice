import sys
import re

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        return

    input_file = sys.argv[1]
    output_file = "words.txt"

    try:
        with open(input_file, "r", encoding="utf-8") as infile, \
             open(output_file, "w", encoding="utf-8") as outfile:

            for line in infile:
                match = re.search(r'text="([^"]+)"', line)
                if match:
                    outfile.write(match.group(1) + "\n")

        print(f"✅ Extracted text saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
