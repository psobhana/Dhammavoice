import sys

def process_file(input_filename):
    output_filename = "words.txt"
    
    try:
        # Open input file for reading and output file for writing, both as utf-8
        with open(input_filename, 'r', encoding='utf-8') as f_in, \
             open(output_filename, 'w', encoding='utf-8') as f_out:
            
            for line in f_in:
                # Add # to the beginning of the line
                # We use end='' because the original line already contains a newline character
                f_out.write(f"#{line}")
                
                # Handling edge case: if the last line has no newline, ensure formatting is consistent
                if not line.endswith('\n'):
                     f_out.write('\n')
                    
        print(f"Successfully processed '{input_filename}' and created '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Check if filename argument is provided
    if len(sys.argv) < 2:
        print("Usage: python add_hash.py <input_file>")
    else:
        process_file(sys.argv[1])
