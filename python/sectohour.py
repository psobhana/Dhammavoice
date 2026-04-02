# Open input and output files in UTF-8
with open("times-temp2.txt", "r", encoding="utf-8") as infile, \
     open("times.txt", "w", encoding="utf-8") as outfile:

    for line in infile:
        line = line.strip()
        if not line:
            continue  # skip empty lines

        seconds = int(line)

        # Convert seconds to hh:mm:ss
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        secs = seconds % 60

        # Format and write
        formatted_time = f"{hours}:{minutes:02}:{secs:02}"
        outfile.write(formatted_time + "\n")