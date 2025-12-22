from datetime import datetime

def add_time_differences(input_file, output_file):
    # standard format H:M:S (e.g., 1:26:00)
    time_format = "%H:%M:%S"
    
    with open(input_file, 'r', encoding='utf-8') as f_in, \
         open(output_file, 'w', encoding='utf-8') as f_out:
        
        # Read lines and remove whitespace
        lines = [line.strip() for line in f_in if line.strip()]
        
        if not lines:
            return

        # Process the first line
        prev_time_str = lines[0]
        try:
            prev_time = datetime.strptime(prev_time_str, time_format)
            # Write the first timestamp
            f_out.write(prev_time_str + "\n")
        except ValueError:
            print(f"Error parsing format for: {prev_time_str}")
            return

        # Iterate through the rest of the lines
        for i in range(1, len(lines)):
            curr_time_str = lines[i]
            try:
                curr_time = datetime.strptime(curr_time_str, time_format)
                
                # Calculate difference
                diff = curr_time - prev_time
                
                # Write difference with dashes
                f_out.write(f"--{diff}\n")
                
                # Write current timestamp
                f_out.write(curr_time_str + "\n")
                
                # Update previous time for next iteration
                prev_time = curr_time
                
            except ValueError:
                print(f"Error parsing format for: {curr_time_str}")
                continue

# Usage
if __name__ == "__main__":
    add_time_differences('times.txt', 'times-dif.txt')
