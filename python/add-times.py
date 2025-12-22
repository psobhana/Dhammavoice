import re

def main():
    # 1. Read the data from times-temp.txt
    start_stop_pairs = []
    last_line_value = ""

    try:
        with open("times-temp.txt", "r", encoding="utf-8") as f:
            # Read all non-empty lines
            lines = [line.strip() for line in f if line.strip()]
            
            if not lines:
                print("Error: times-temp.txt is empty.")
                return

            # Store the last line for loadYoutubeStart
            last_line_value = lines[-1]

            # Process lines for loadYoutubeStartStop (looking for pairs)
            for line in lines:
                parts = line.split(',')
                if len(parts) >= 2:
                    start_stop_pairs.append((parts[0].strip(), parts[1].strip()))
                    
    except FileNotFoundError:
        print("Error: times-temp.txt not found.")
        return

    # Create an iterator for the pairs
    times_iterator = iter(start_stop_pairs)

    # 2. Read output.html
    try:
        with open("output.html", "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print("Error: output.html not found.")
        return

    # 3. Define the replacement function for StartStop
    def replace_start_stop(match):
        try:
            new_start, new_end = next(times_iterator)
            video_id = match.group(1)
            return f"javascript:loadYoutubeStartStop('{video_id}', {new_start}, {new_end})"
        except StopIteration:
            return match.group(0)

    # 4. Define the replacement function for Start
    def replace_start(match):
        video_id = match.group(1)
        # Use the stored last line value
        return f"javascript:loadYoutubeStart('{video_id}', {last_line_value})"

    # 5. Perform Replacements
    
    # Replace loadYoutubeStartStop (Two arguments)
    # Pattern: func('ID', digit, digit)
    pattern_start_stop = r"javascript:loadYoutubeStartStop\('([^']*)',\s*\d+,\s*\d+\)"
    content = re.sub(pattern_start_stop, replace_start_stop, content)

    # Replace loadYoutubeStart (One argument)
    # Pattern: func('ID', digit)
    pattern_start = r"javascript:loadYoutubeStart\('([^']*)',\s*\d+\)"
    content = re.sub(pattern_start, replace_start, content)

    # 6. Write to output2.html
    with open("output2.html", "w", encoding="utf-8") as f:
        f.write(content)
    
    print("Successfully created output2.html")

if __name__ == "__main__":
    main()
