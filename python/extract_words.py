import sys
import re

def process_file(input_filename):
    output_filename = "words.txt"
    
    # Regex explanation:
    # 1. <button[^>]*: Finds the start of a button tag
    # 2. onclick="loadYoutube2\('([^']+)'\)": Finds the specific function and captures the ID (Group 1)
    # 3. [^>]*>: Matches the rest of the opening tag
    # 4. (.*?)</button>: Captures the text content inside the button (Group 2)
    pattern = re.compile(r"<button[^>]*onclick=\"loadYoutube2\('([^']+)'\)\"[^>]*>(.*?)</button>")

    try:
        with open(input_filename, 'r', encoding='utf-8') as f_in, \
             open(output_filename, 'w', encoding='utf-8') as f_out:
            
            for line in f_in:
                match = pattern.search(line)
                if match:
                    video_id = match.group(1)
                    button_text = match.group(2)
                    # Write to file in format: Text, ID
                    f_out.write(f"{button_text}, {video_id}\n")
                    
        print(f"Successfully processed '{input_filename}' and created '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Check if filename argument is provided
    if len(sys.argv) < 2:
        print("Usage: python extract_words.py <input_file>")
    else:
        process_file(sys.argv[1])
