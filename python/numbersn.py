import sys

def add_line_numbers(file_path, start_number):
    try:
        # Open the file in read mode with UTF-8 encoding
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # Determine the digit width based on the total number of lines and starting number
        total_lines = len(lines)
        digit_width = len(str(int(start_number) + total_lines - 1))
        
        # Add line numbers to non-empty lines with leading zeros in start_number
        numbered_lines = [
            f"{str(int(start_number) + i).zfill(len(start_number))}. {line}" if line.strip() else line
            for i, line in enumerate(lines)
        ]
        
        # Save the updated lines back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(numbered_lines)
        
        print("Line numbers added successfully!")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except ValueError:
        print("Error: Starting number must be an integer.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <file_path> <start_number>")
    else:
        file_path = sys.argv[1]
        try:
            start_number = sys.argv[2]
            add_line_numbers(file_path, start_number)
        except ValueError:
            print("Error: Starting number must be an integer.")
