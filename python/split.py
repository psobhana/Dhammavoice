def split_words_file(input_filename='words.txt', output_left='input.txt', output_right='input2.txt'):
    """
    Splits each line at the first '(' character.
    Left part goes to output_left, right part (including '(') goes to output_right.
    All files use UTF-8 encoding.
    """
    try:
        # Open input file with UTF-8 encoding
        with open(input_filename, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
        
        left_parts = []
        right_parts = []
        
        for line in lines:
            # Strip trailing newline for processing
            line = line.rstrip('\n')
            
            # Find the first left parenthesis
            if '(' in line:
                left, right = line.split('(', 1)
                # Strip whitespace from left part, add back the '(' to right part
                left_parts.append(left.strip())
                right_parts.append('(' + right)
            else:
                # No parenthesis found, entire line goes to left file
                left_parts.append(line.strip())
                right_parts.append('')  # Empty line for right file
        
        # Write left parts to output_left
        with open(output_left, 'w', encoding='utf-8') as outfile:
            for part in left_parts:
                outfile.write(part + '\n')
        
        # Write right parts to output_right
        with open(output_right, 'w', encoding='utf-8') as outfile:
            for part in right_parts:
                outfile.write(part + '\n')
        
        print(f"✓ Successfully split '{input_filename}' into:")
        print(f"  - '{output_left}' ({len(left_parts)} lines)")
        print(f"  - '{output_right}' ({len(right_parts)} lines)")
        
    except FileNotFoundError:
        print(f"✗ Error: '{input_filename}' not found.")
    except Exception as e:
        print(f"✗ Error: {e}")

# Run the function
split_words_file()