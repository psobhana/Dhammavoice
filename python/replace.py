import sys

def replace_in_file(filename, search_string, replace_string):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        updated_content = content.replace(search_string, replace_string)
        
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(updated_content)
        
        print(f"Replaced '{search_string}' with '{replace_string}' in {filename}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python replace.py file.xml search_string replace_string")
        sys.exit(1)
    
    _, filename, search_string, replace_string = sys.argv
    replace_in_file(filename, search_string, replace_string)
