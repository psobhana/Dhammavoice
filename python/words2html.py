import re
from itertools import zip_longest

SUMMARY_PATTERN = re.compile(r"<summary>.*?</summary>", re.DOTALL)
BUTTON_PATTERN = re.compile(r"(<button[^>]*>)(.*?)(</button>)")

SKIP_LINE = "</ul></details></li>\n"  # exact line to skip (with newline)

def main():
    # Read replacement words (one per line)
    with open("words.txt", "r", encoding="utf-8") as f_words:
        words = [line.rstrip("\n") for line in f_words]

    with open("input.html", "r", encoding="utf-8") as f_in, \
         open("output.html", "w", encoding="utf-8") as f_out:

        word_index = 0  # manual index instead of zip_longest

        for line in f_in:
            # If this is the special line, write as-is and do NOT consume a word
            if line == SKIP_LINE:
                f_out.write(line)
                continue

            # If we still have a word to use, apply replacement
            if word_index < len(words):
                word = words[word_index]

                if "<summary>" in line:
                    new_line = SUMMARY_PATTERN.sub(f"<summary>{word}</summary>", line, count=1)
                    word_index += 1
                elif "<button" in line:
                    def replace_button(match):
                        return match.group(1) + word + match.group(3)
                    new_line = BUTTON_PATTERN.sub(replace_button, line, count=1)
                    word_index += 1
                else:
                    new_line = line
            else:
                new_line = line

            f_out.write(new_line)

    print("Done! Output written to output.txt")

if __name__ == "__main__":
    main()
