import sys
import re

def process_file(input_file, output_file):
    """
    Process the input file:
    - Remove XML header
    - Remove tree-related tags
    - Truncate each line at the first '('
    - Remove all empty lines
    - Ensure no empty first line
    - Remove all numbers and dots
    - Remove leading spaces
    
    :param input_file: Path to the input file
    :param output_file: Path to the output file
    """
    try:
        # Read the input file with UTF-8 encoding
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Remove XML header
        content = content.replace('<?xml version="1.0" encoding="UTF-8"?>', '')
        content = content.replace('<?xml version="1.0" encoding="UTF8"?>', '')
        
        # Remove <tree> tags (opening and text variations)
        content = content.replace('<tree>', '')
        content = content.replace('<tree text="', '')
        content = content.replace('</tree>', '')
        
        # Split into lines
        lines = content.splitlines()
        
        # Process lines
        processed_lines = []
        for line in lines:
            # Split at first '(' and take the first part
            processed_line = line.split('(')[0].strip()
            
            # Remove all numbers and dots
            processed_line = re.sub(r'[0-9.]', '', processed_line)
            
            # Remove leading and trailing spaces
            processed_line = processed_line.strip()
            
            # Only add non-empty lines
            if processed_line:
                processed_lines.append(processed_line + '\n')
        
        # Ensure the first line is not empty
        while processed_lines and not processed_lines[0].strip():
            processed_lines.pop(0)
        
        # Write the processed lines to the output file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.writelines(processed_lines)
        
        # Now process the output file to remove first and last 0D and 0A
        with open(output_file, 'rb') as file:
            content = file.read()
        
        # Remove first occurrence of hex 0D and 0A
        content = content.replace(b'\x0D', b'', 1)
        content = content.replace(b'\x0A', b'', 1)
        
        # Remove last occurrence of hex 0D and 0A
        content = content[:-1].rstrip(b'\x0D\x0A') + content[-1:]
        
        # Write back to the output file
        with open(output_file, 'wb') as file:
            file.write(content)
        
        print(f"Successfully processed {input_file}. Output written to {output_file}")
    
    except FileNotFoundError:
        print(f"Error: File {input_file} not found.")
    except PermissionError:
        print(f"Error: Permission denied when trying to read {input_file} or write {output_file}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    # Check if correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)
    
    # Get input file path from command line argument
    input_file = sys.argv[1]
    
    # Set output file name
    output_file = 'words.txt'
    
    # Call the function to process the file
    process_file(input_file, output_file)

if __name__ == "__main__":
    main()