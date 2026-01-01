import sys
import re

def process_file(filename):
    try:
        # 1. Open the file as a command line argument
        # 2. Open the file as utf-8
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Dictionary to store indices: { '1': [0, 2], '2': [1, 3] }
        occurrences = {}
        
        # Regex to find lines starting with a number followed by a dot (e.g., "1. ")
        number_pattern = re.compile(r'^(\d+)\.')

        # Scan finding all line numbers
        for index, line in enumerate(lines):
            match = number_pattern.match(line.strip())
            if match:
                number = match.group(1)
                if number not in occurrences:
                    occurrences[number] = []
                occurrences[number].append(index)

        lines_modified = False

        # 3. Copy the words in second line with matching number to the first line
        for number, indices in occurrences.items():
            # We strictly need at least two occurrences to perform a copy
            if len(indices) >= 2:
                first_idx = indices[0]   # The Target (to be overwritten)
                second_idx = indices[1]  # The Source (READ-ONLY)

                # Capture the content of the second location
                # We use string slicing or copy to ensure we don't reference the memory address
                source_content = lines[second_idx]

                # Safety check: Ensure we handle newlines correctly if source was end-of-file
                # If the source line has no newline but is moving to a position that needs one:
                if not source_content.endswith('\n') and first_idx < len(lines) - 1:
                    source_content += '\n'

                # Overwrite the first location ONLY. 
                # The line at 'second_idx' is untouched.
                lines[first_idx] = source_content
                lines_modified = True

        # Write results
        if lines_modified:
            with open(filename, 'w', encoding='utf-8') as file:
                file.writelines(lines)
            print(f"Successfully processed '{filename}'.")
        else:
            print("No matching second occurrences found.")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python replace_match.py <filename>")
    else:
        process_file(sys.argv[1])
