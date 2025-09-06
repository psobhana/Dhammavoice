import sys
import re

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = "words.txt"

    #!/usr/bin/env python3
import sys
import re

def main():
    if len(sys.argv) < 3:
        print("Usage: python extract_playlist.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Match only "javascript:loadYoutubePlaylistLoop(...)"
    pattern = re.compile(r"javascript:loadYoutubePlaylistLoop\([^)]*\);")

    results = []

    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            match = pattern.search(line)
            if match:
                results.append(match.group(0))

    with open(output_file, "w", encoding="utf-8") as f:
        for item in results:
            f.write(item + "\n")

    print(f"✅ Done — extracted {len(results)} matches to {output_file}")

if __name__ == "__main__":
    main()
