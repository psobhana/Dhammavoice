import re

input_file = "input.html"
output_file = "times-temp.txt"

# Patterns
pattern_start_stop = r"loadYoutubeStartStop\((.*?)\)"
pattern_start = r"loadYoutubeStart\((.*?)\)"

results = []

# Read file as UTF-8
with open(input_file, "r", encoding="utf-8") as f:
    content = f.read()

# Find matches
matches = re.findall(pattern_start_stop, content) + re.findall(pattern_start, content)

# Process each match
for match in matches:
    parts = [p.strip() for p in match.split(",")]

    # Remove first variable (YouTube ID)
    remaining = parts[1:]

    # Join remaining values
    results.append(", ".join(remaining))

# Write output as UTF-8
with open(output_file, "w", encoding="utf-8") as f:
    for line in results:
        f.write(line + "\n")

print("Done. First variable removed.")