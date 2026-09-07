import sys
import re

def lowercase_cyrillic_only(text):
    # This regex matches one or more consecutive Cyrillic characters.
    # It completely ignores English words, numbers, and punctuation.
    cyrillic_pattern = r'[\u0400-\u04FF]+'
    
    # re.sub finds every Cyrillic match and applies .lower() to it
    return re.sub(cyrillic_pattern, lambda match: match.group(0).lower(), text)

def main():
    if len(sys.argv) < 2:
        print("Error: Please provide the input file path.")
        print("Usage: python script.py <input_file.txt>")
        sys.exit(1)
        
    input_filename = sys.argv[1]
    output_filename = "output.txt"

    try:
        with open(input_filename, 'r', encoding='utf-8') as infile, \
             open(output_filename, 'w', encoding='utf-8') as outfile:
            
            for line in infile:
                processed_line = lowercase_cyrillic_only(line)
                outfile.write(processed_line)
                
        print(f"Success! Only Cyrillic text has been lowercased in {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' could not be found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
