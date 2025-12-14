import re
from itertools import zip_longest

SUMMARY_PATTERN = re.compile(r"<summary>.*?</summary>", re.DOTALL)

def main():
    # Read replacement words (one per line)
    with open("words.txt", "r", encoding="utf-8") as f_words:
        words = [line.rstrip("\n") for line in f_words]

    with open("input.txt", "r", encoding="utf-8") as f_in, \
         open("output.txt", "w", encoding="utf-8") as f_out:

        for line, word in zip_longest(f_in, words, fillvalue=None):
            if line is None:
                break
            if word is not None:
                # replace whatever is between <summary> and </summary>
                new_line = SUMMARY_PATTERN.sub(f"<summary>{word}</summary>", line, count=1)
            else:
                new_line = line
            f_out.write(new_line)

if __name__ == "__main__":
    main()
