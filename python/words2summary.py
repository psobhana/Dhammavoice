import sys
import re

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_file>")
        return

    input_file = sys.argv[1]
    output_file = "output2.txt"
    word_file = "words.txt"

    try:
        # Read replacement words
        with open(word_file, "r", encoding="utf-8") as wf:
            replacements = [line.strip() for line in wf if line.strip()]

        with open(input_file, "r", encoding="utf-8") as infile, \
             open(output_file, "w", encoding="utf-8") as outfile:

            i = 0  # index for replacements
            for line in infile:
                if "<summary>" in line and "</summary>" in line and i < len(replacements):
                    line = re.sub(
                        r"<summary>.*?</summary>",
                        f"<summary>{replacements[i]}</summary>",
                        line
                    )
                    i += 1
                outfile.write(line)

        print(f"✅ Processed file saved to {output_file}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
