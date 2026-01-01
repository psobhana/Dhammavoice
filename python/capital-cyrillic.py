import sys
import re

def process_file(filename):
    try:
        # 1. Open the file as command line argument
        # 2. Open the file as utf-8
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        occurrences = {}
        # Regex to capture the number at the start of the line (e.g., "1.", "20.")
        number_pattern = re.compile(r'^(\d+)\.')

        # Scan for line numbers
        for index, line in enumerate(lines):
            match = number_pattern.match(line.strip())
            if match:
                number = match.group(1)
                if number not in occurrences:
                    occurrences[number] = []
                occurrences[number].append(index)

        lines_modified = False

        # 3. Copy words from second line (except first letter) to the first line
        for number, indices in occurrences.items():
            if len(indices) >= 2:
                first_idx = indices[0]   # Target
                second_idx = indices[1]  # Source

                # Split lines into word parts
                # We use split() which handles multiple spaces as a single delimiter
                target_parts = lines[first_idx].strip().split()
                source_parts = lines[second_idx].strip().split()

                # Start the new line with the number (e.g., "1.")
                # We assume the first part (index 0) is the number "1."
                new_line_parts = [target_parts[0]]

                # The words start from index 1 (after the "1.")
                # We iterate based on the SOURCE line's word count, 
                # as the instruction implies copying the structure of the second line.
                max_words = len(source_parts)
                
                for i in range(1, max_words):
                    source_word = source_parts[i]
                    
                    # If the target line has a corresponding word, use its first letter
                    if i < len(target_parts):
                        target_char = target_parts[i][0] # First letter of target
                        rest_of_source = source_word[1:] # Source word minus first letter
                        new_word = target_char + rest_of_source
                    else:
                        # If target is shorter than source, just copy the source word as is
                        new_word = source_word
                    
                    new_line_parts.append(new_word)

                # Reconstruct the line
                # Join with spaces and add the newline character back
                lines[first_idx] = " ".join(new_line_parts) + "\n"
                lines_modified = True

        if lines_modified:
            with open(filename, 'w', encoding='utf-8') as file:
                file.writelines(lines)
            print(f"Successfully processed '{filename}'.")
        else:
            print("No matching numbered lines found to process.")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python hybrid_copy.py <filename>")
    else:
        process_file(sys.argv[1])
