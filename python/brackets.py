import re
import sys

# Check if the script has received enough command-line arguments
if len(sys.argv) < 2:
    print("Usage: python script.py <xml_file>")
    sys.exit(1)

# File name from command-line argument
xml_file = sys.argv[1]  # Get the XML file name from the command line

# Read the content of the XML file using UTF-8 encoding
with open(xml_file, "r", encoding="utf-8") as file:
    xml_content = file.readlines()

# Function to remove text between [space]( and )
def remove_text_in_line(line):
    # Use regular expression to find and remove text between [space]( and )
    return re.sub(r' \(.*?\)', '', line)

# Function to replace " src=" with " ()" src="
def replace_src_in_line(line):
    # Use regular expression to find " src=" and replace it with " ()" src="
    return re.sub(r'" src=', ' ()" src=', line)

# Process each line in the XML content
for i in range(len(xml_content)):
    # Remove text between [space]( and ) if it exists
    xml_content[i] = remove_text_in_line(xml_content[i])
    # Replace " src=" with " ()" src="
    xml_content[i] = replace_src_in_line(xml_content[i])

# Write the updated content back to the XML file using UTF-8 encoding
with open(xml_file, "w", encoding="utf-8") as file:
    file.writelines(xml_content)

print(f"The text between [space]( and ) has been successfully removed, and ' src=' has been replaced in {xml_file}.")