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

    # Regex to capture YouTube ID and up to 2 numbers
    pattern = re.compile(
        r"javascript:(?:loadYoutubeStartStop|loadYoutubeStart)\(\s*'([^']+)'\s*(?:,\s*([0-9]+))?(?:,\s*([0-9]+))?\s*\)"
    )

    for line in lines:
        match = pattern.search(line)
        if match:
            # Collect values (ID + numbers), skip None values
            values = [match.group(1)] + [g for g in match.groups()[1:] if g]
            extracted.append(", ".join(values))  # add space after commas

    # Write the output to words.txt
    with open("words.txt", "w", encoding="utf-8") as f:
        for item in extracted:
            f.write(item + "\n")

    print(f"✅ Done. Extracted {len(extracted)} entries written to words.txt")

if __name__ == "__main__":
    main()
