import re

def process_html_file(input_filename, output_filename):
    """
    Reads an input HTML file, copies arguments from specific source JS functions
    to target JS functions on the same line, and writes to an output file.
    """
    
    # Define regex patterns
    # Pattern 1: Capture args from loadYoutubeStartStop and find the sharePageSrartStop to replace
    # We look for:
    # 1. javascript:loadYoutubeStartStop('ID', start, end) -> Capture group 1 (the args)
    # 2. Any text in between (lazy match) -> Group 2
    # 3. sharePageSrartStop(...) -> We want to replace the args inside this
    pattern_start_stop = r"(javascript:loadYoutubeStartStop\(([^)]+)\))(.*?)(sharePageSrartStop\([^)]+\))"
    
    # Pattern 2: Capture args from loadYoutubeStart and find the sharePageSrart to replace
    pattern_start = r"(javascript:loadYoutubeStart\(([^)]+)\))(.*?)(sharePageSrart\([^)]+\))"

    try:
        with open(input_filename, 'r', encoding='utf-8') as infile, \
             open(output_filename, 'w', encoding='utf-8') as outfile:
            
            for line in infile:
                # Apply replacement for StartStop function
                # \1 restores the full load... function
                # \3 restores the text in between
                # sharePageSrartStop(\2) inserts the captured args from load... into share...
                new_line = re.sub(pattern_start_stop, r"\1\3sharePageSrartStop(\2)", line)
                
                # Apply replacement for Start function
                new_line = re.sub(pattern_start, r"\1\3sharePageSrart(\2)", new_line)
                
                outfile.write(new_line)
                
        print(f"Successfully processed '{input_filename}' and created '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Execute the function
if __name__ == "__main__":
    process_html_file("output2.html", "output3.html")
