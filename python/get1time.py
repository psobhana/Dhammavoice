# Open input file and output file with UTF-8 encoding
with open("times-temp.txt", "r", encoding="utf-8") as infile, \
     open("times-temp2.txt", "w", encoding="utf-8") as outfile:

    for line in infile:
        line = line.strip()

        if not line:
            continue  # skip empty lines

        # Split by comma
        parts = line.split(",")

        # Take only the first number
        first_number = parts[0].strip()

        # Write to output file
        outfile.write(first_number + "\n")