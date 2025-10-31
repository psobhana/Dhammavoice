import sys
import re

if len(sys.argv) < 2:
    print("Usage: python script.py filename")
    sys.exit(1)

filename = sys.argv[1]

load_pattern = re.compile(r"loadYoutube2\('([^']+)'\)")
share_pattern = re.compile(r"sharePage\('([^']+)'\)")

with open(filename, encoding='utf-8') as f, open('words.txt', 'w', encoding='utf-8') as out:
    for idx, line in enumerate(f, start=1):
        load_match = load_pattern.search(line)
        share_match = share_pattern.search(line)
        if load_match and share_match:
            var1 = load_match.group(1)
            var2 = share_match.group(1)
            if var1 != var2:
                out.write(f"{idx}\n")
