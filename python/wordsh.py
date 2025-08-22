import re
import sys

# Check if the script has received enough command-line arguments
if len(sys.argv) < 2:
    print("Usage: python script.py <xml_file>")
    sys.exit(1)

# File names from command-line arguments
xml_file = sys.argv[1]  # Get the XML file name from the command line
words_file = "words.txt"

# Read the lines from words.txt using UTF-8 encoding
with open(words_file, "r", encoding="utf-8") as file:
    words_lines = file.readlines()

# Read the content of the XML file using UTF-8 encoding
with open(xml_file, "r", encoding="utf-8") as file:
    xml_content = file.readlines()

# Function to replace text in each line based on words.txt
def replace_text_in_line(line, replacement_text):
    # Add a space to the replacement text
    # replacement_text += ' '  # Add a space after the word (removed for headings)

    # Use regular expression to find <tree text=" and " part
    match = re.search(r'(<tree text=")(.*?)(\")', line)
    if match:
        # Construct the new line with the replacement text and leave the rest unchanged
        return match.group(1) + replacement_text + match.group(3) + line[match.end(3):]
    return line  # Return the line unchanged if no match

# Replace the text in the XML file with the corresponding lines from words.txt
words_line_index = 0  # Start with the first line in words.txt
for i in range(len(xml_content)):
    # Ignore lines before finding <tree text=".
    if "<tree text=\"" in xml_content[i]:
        # Replace the text if the line contains <tree text=".
        if words_line_index < len(words_lines):
            xml_content[i] = replace_text_in_line(xml_content[i], words_lines[words_line_index].strip())
            words_line_index += 1  # Move to the next line in words.txt

# Write the updated content back to the XML file using UTF-8 encoding
with open(xml_file, "w", encoding="utf-8") as file:
    file.writelines(xml_content)

print(f"The text has been successfully replaced in {xml_file}.")
