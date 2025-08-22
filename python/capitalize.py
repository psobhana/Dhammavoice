import sys

def capitalize_words_in_file(input_file):
    try:
        with open(input_file, 'r+', encoding='utf-8') as file:
            content = file.read()

            # Capitalize the first letter of each word
            capitalized_content = content.title()

            # Move the file pointer to the beginning and overwrite the file
            file.seek(0)
            file.write(capitalized_content)
            file.truncate()  # Remove any leftover content if new data is shorter

        print(f"Words in '{input_file}' have been capitalized.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
    else:
        input_file = sys.argv[1]
        capitalize_words_in_file(input_file)
