import sys
import re

def replace_numbers_in_file(file_path):
    """
    Modify the input file in-place, replacing:
    1. Numbers in (Xmin.) with (00min.)
    2. Numbers between ', ' and 'p' with 00
    
    :param file_path: Path to the file to be modified
    """
    try:
        # Open the file with UTF-8 encoding
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # First replace numbers in (Xmin.) format with 00
        modified_content = re.sub(r'\((\d+)min\.\)', r'(00min.)', content)
        
        # Then replace numbers between ', ' and 'p'
        modified_content = re.sub(r', (\d+)p', r', 00p', modified_content)
        
        # Write the modified content back to the same file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(modified_content)
        
        print(f"Successfully modified {file_path}")
    
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
    except PermissionError:
        print(f"Error: Permission denied when trying to modify {file_path}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    # Check if correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)
    
    # Get input file path from command line argument
    file_path = sys.argv[1]
    
    # Call the function to modify the file
    replace_numbers_in_file(file_path)

if __name__ == "__main__":
    main()