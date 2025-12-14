import re
from itertools import zip_longest

SUMMARY_PATTERN = re.compile(r"<summary>.*?</summary>", re.DOTALL)
BUTTON_PATTERN = re.compile(r"(<button[^>]*>)(.*?)(</button>)")

def main():
    # Read replacement words (one per line)
    with open("words.txt", "r", encoding="utf-8") as f_words:
        words = [line.rstrip("\n") for line in f_words]

    with open("input.html", "r", encoding="utf-8") as f_in, \
         open("output.html", "w", encoding="utf-8") as f_out:

        for line, word in zip_longest(f_in, words, fillvalue=None):
            if line is None:
                break
            
            if word is not None:
                # Check if line contains <summary> or <button>
                if "<summary>" in line:
                    new_line = SUMMARY_PATTERN.sub(f"<summary>{word}</summary>", line, count=1)
                elif "<button" in line:
                    def replace_button(match):
                        return match.group(1) + word + match.group(3)
                    new_line = BUTTON_PATTERN.sub(replace_button, line, count=1)
                else:
                    new_line = line
            else:
                new_line = line
            
            f_out.write(new_line)

    print("Done! Output written to output.txt")

if __name__ == "__main__":
    main()
