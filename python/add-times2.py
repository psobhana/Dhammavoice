import re

def main():
    # 1. Read the new times from times-temp.txt
    replacement_times = []
    try:
        with open("times-temp.txt", "r", encoding="utf-8") as f:
            for line in f:
                # Remove whitespace and split by comma
                parts = line.strip().split(',')
                if len(parts) >= 2:
                    # Store (start, stop) tuple
                    replacement_times.append((parts[0].strip(), parts[1].strip()))
    except FileNotFoundError:
        print("Error: times-temp.txt not found.")
        return

    # Create an iterator to fetch times one by one
    times_iterator = iter(replacement_times)

    # 2. Read the content of output.html
    try:
        with open("output.html", "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print("Error: output.html not found.")
        return

    # 3. Define the replacement logic
    def replace_func(match):
        try:
            # Get the next available time pair
            new_start, new_end = next(times_iterator)
            
            # Group 1 captures the ID (e.g., '3YHgOJvAxDw') from the regex below
            video_id = match.group(1)
            
            # Return the reconstructed string
            return f"javascript:loadYoutubeStartStop('{video_id}', {new_start}, {new_end})"
        except StopIteration:
            # If we run out of replacement times, leave the original text unchanged
            return match.group(0)

    # 4. Regex Pattern Explanation:
    # javascript:loadYoutubeStartStop\(  -> Matches literal function name and opening paren
    # '([^']*)'                          -> Group 1: Matches and captures the Video ID
    # ,\s*\d+                            -> Matches comma, optional space, and old start time digits
    # ,\s*\d+                            -> Matches comma, optional space, and old end time digits
    # \)                                 -> Matches literal closing paren
    pattern = r"javascript:loadYoutubeStartStop\('([^']*)',\s*\d+,\s*\d+\)"

    # Perform the substitution
    new_content = re.sub(pattern, replace_func, content)

    # 5. Write the result to output2.html
    with open("output2.html", "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print("Successfully created output2.html")

if __name__ == "__main__":
    main()
