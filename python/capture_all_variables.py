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

    # Regex patterns
    patterns = [
        # Matches: loadYoutubeStartStop('ID', num, num) or loadYoutubeStart('ID', num)
        re.compile(
            r"javascript:(?:loadYoutubeStartStop|loadYoutubeStart)\(\s*'([^']+)'\s*(?:,\s*([0-9]+))?(?:,\s*([0-9]+))?\s*\)"
        ),
        # Matches: loadYoutubePlaylistLoop('PLAYLIST_ID', true/false/number)
        re.compile(
            r"javascript:loadYoutubePlaylistLoop\(\s*'([^']+)'\s*,\s*([^)\s]+)\s*\)"
        ),
    ]

    for line in lines:
        for pattern in patterns:
            match = pattern.search(line)
            if match:
                # Collect values, skip None values
                values = [match.group(1)] + [g for g in match.groups()[1:] if g]
                extracted.append(", ".join(values))
                break  # stop at first matching pattern for this line

    # Write the output to words.txt
    with open("words.txt", "w", encoding="utf-8") as f:
        for item in extracted:
            f.write(item + "\n")

    print(f"✅ Done. Extracted {len(extracted)} entries written to words.txt")

if __name__ == "__main__":
    main()
