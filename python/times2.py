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

# Main Script Execution
# Note: The XML file argument check was removed since XML processing is no longer part of this script.
# If you still want to require an argument for future use, you can keep the check.
# I have kept the file path definitions but removed the XML argument requirement logic as it is now unused.

times_file_path = "times.txt"  # Input file with raw times
temp_times_file_path = "times-temp.txt"  # Temporary processed times file

# Step 1: Process times and save to temp file
process_times(times_file_path, temp_times_file_path)
