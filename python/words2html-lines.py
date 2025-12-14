import re

# Read words from words.txt
with open('words.txt', 'r', encoding='utf-8') as f:
    words = f.read().splitlines()

# Read lines from input.txt
with open('input.txt', 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()

# Process each line and replace text in the first button
output_lines = []
for i, line in enumerate(lines):
    if i < len(words):
        # Pattern to match the first <button...>text</button>
        pattern = r'(<button[^>]*>)(.*?)(</button>)'
        
        # Use a function for replacement to avoid issues with special characters
        def replace_first(match):
            return match.group(1) + words[i] + match.group(3)
        
        new_line = re.sub(pattern, replace_first, line, count=1)
        output_lines.append(new_line)
    else:
        output_lines.append(line)

# Write to output.txt
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output_lines))

print("Done! Output written to output.txt")
