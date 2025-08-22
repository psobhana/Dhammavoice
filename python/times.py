import re
import sys

def time_to_seconds(time_str):
    """
    Convert time in HH:MM:SS format to seconds.

    Args:
        time_str (str): Time in HH:MM:SS format.

    Returns:
        int: Total time in seconds.
    """
    try:
        # Split the time string into hours, minutes, and seconds
        hours, minutes, seconds = map(int, time_str.strip().split(':'))
        return hours * 3600 + minutes * 60 + seconds
    except ValueError:
        raise ValueError(f"Invalid time format: '{time_str}'")

def process_times(input_file, output_file):
    """
    Process times from a file, convert to seconds, and create a combined output format.

    Args:
        input_file (str): Path to the input file containing times.
        output_file (str): Path to the output file for combined output.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
            lines = infile.readlines()
            for i in range(len(lines)):
                time_str = lines[i].strip()
                if time_str:  # Ignore empty lines
                    seconds = time_to_seconds(time_str)
                    if i < len(lines) - 1:  # For all lines except the last
                        next_time = lines[i + 1].strip()
                        if next_time:
                            seconds_next = time_to_seconds(next_time)
                            outfile.write(f"{seconds}, {seconds_next}\n")
                        else:
                            outfile.write(f"{seconds}\n")
                    else:  # For the last line, no additional processing
                        outfile.write(f"{seconds}\n")

        print(f"Processed times saved to {output_file}.")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to replace text between ', and ); and prepend text before ',.
def prepend_and_replace_text(line, replacement_text):
    # Match text before ', and text between ', and );
    match = re.search(r'(.*?)(\',)(.*?)(\);)', line)
    if match:
        # Extract the text before ', (group 1)
        text_before_comma = match.group(1)
        # Add a space after ', and construct the updated line
        return text_before_comma + match.group(2) + " " + replacement_text + match.group(4) + line[match.end(4):]
    return line  # Return the line unchanged if no match

def update_xml_with_times(xml_file, words_file):
    """
    Update an XML file with times processed from a temporary file.

    Args:
        xml_file (str): Path to the XML file to be updated.
        words_file (str): Path to the processed times file.
    """
    # Read the lines from times-temp.txt using UTF-8 encoding
    with open(words_file, "r", encoding="utf-8") as file:
        words_lines = file.readlines()

    # Read the content of the XML file using UTF-8 encoding
    with open(xml_file, "r", encoding="utf-8") as file:
        xml_content = file.readlines()

    # Replace the text in the XML file with the corresponding lines from words.txt
    words_line_index = 0  # Start with the first line in words.txt
    for i in range(len(xml_content)):
        if "'," in xml_content[i] and ");" in xml_content[i]:  # Ensure line contains both ', and );
            if words_line_index < len(words_lines):  # Ensure there are lines left in words.txt
                replacement_text = words_lines[words_line_index].strip()
                xml_content[i] = prepend_and_replace_text(xml_content[i], replacement_text)
                words_line_index += 1  # Move to the next line in words.txt

    # Write the updated content back to the XML file using UTF-8 encoding
    with open(xml_file, "w", encoding="utf-8") as file:
        file.writelines(xml_content)

    print(f"The text has been successfully replaced and prepended in {xml_file}.")

# Main Script Execution
if len(sys.argv) < 2:
    print("Usage: python script.py <xml_file>")
    sys.exit(1)

xml_file_path = sys.argv[1]  # XML file name from the command line
times_file_path = "times.txt"  # Input file with raw times
temp_times_file_path = "times-temp.txt"  # Temporary processed times file

# Step 1: Process times and save to temp file
process_times(times_file_path, temp_times_file_path)

# Step 2: Update XML file with processed times
update_xml_with_times(xml_file_path, temp_times_file_path)
