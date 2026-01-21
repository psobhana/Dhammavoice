import sys
import csv

def merge_csv_files(file1_path, file2_path):
    output_file = "words.txt"
    
    # Dictionary to store data from the second file for fast lookup
    # Key = Title (2nd column), Value = Full Row
    lookup_data = {}
    
    try:
        # Step 1: Read the second file and build a lookup table
        with open(file2_path, 'r', encoding='utf-8') as f2:
            reader = csv.reader(f2)
            for row in reader:
                if len(row) >= 2:
                    # The second variable is at index 1
                    # using strip() to handle potential surrounding whitespace
                    key = row[1].strip()
                    lookup_data[key] = row
    except FileNotFoundError:
        print(f"Error: The file '{file2_path}' was not found.")
        return

    results = []
    
    try:
        # Step 2: Read the first file and match against the lookup table
        with open(file1_path, 'r', encoding='utf-8') as f1:
            reader = csv.reader(f1)
            for row in reader:
                if len(row) >= 2:
                    key = row[1].strip()
                    
                    # Step 3 & 4: Check for match and merge
                    if key in lookup_data:
                        second_row = lookup_data[key]
                        
                        # Construct the output row:
                        # 1st variable of first file + entire row of second file
                        # Example: [dh085] + [tk_..., Proficiency, QB...]
                        merged_row = [row[0]] + second_row
                        results.append(merged_row)
                        
    except FileNotFoundError:
        print(f"Error: The file '{file1_path}' was not found.")
        return

    # Step 5: Write the output to words.txt
    try:
        with open(output_file, 'w', encoding='utf-8', newline='') as out:
            writer = csv.writer(out)
            writer.writerows(results)
        print(f"Successfully processed files and created '{output_file}'.")
    except Exception as e:
        print(f"An error occurred while writing: {e}")

if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) < 3:
        print("Usage: python merge_csv.py <first.csv> <second.csv>")
    else:
        merge_csv_files(sys.argv[1], sys.argv[2])
