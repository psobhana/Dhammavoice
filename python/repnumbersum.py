import re

# Load replacements from numbers.txt
replacements = {}

with open("numbers.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if "=" in line:
            key, value = line.split("=", 1)
            replacements[key.strip()] = value.strip()

# Process output.html and write to output2.html
with open("output.html", "r", encoding="utf-8") as infile, \
     open("output2.html", "w", encoding="utf-8") as outfile:

    for line in infile:
        def replace_summary(match):
            text = match.group(1)

            # Apply all replacements
            for old, new in sorted(replacements.items(), key=lambda x: len(x[0]), reverse=True):
                text = text.replace(old, new)

            return f"<summary>{text}</summary>"

        line = re.sub(
            r"<summary>(.*?)</summary>",
            replace_summary,
            line,
            flags=re.IGNORECASE
        )

        outfile.write(line)

print("Done. Output written to output2.html")