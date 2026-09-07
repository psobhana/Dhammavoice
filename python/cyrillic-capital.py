import sys
import re

def capitalize_cyrillic_words(text):
    # Match words that start with a Cyrillic letter
    pattern = r'([\u0400-\u04FF])([^\s]*)'

    def repl(match):
        return match.group(1).upper() + match.group(2)

    return re.sub(pattern, repl, text)

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = "output.txt"

    try:
        with open(input_filename, "r", encoding="utf-8") as infile, \
             open(output_filename, "w", encoding="utf-8") as outfile:

            for line in infile:
                outfile.write(capitalize_cyrillic_words(line))

        print(f"Success! Processed text has been written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: File not found: {input_filename}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()