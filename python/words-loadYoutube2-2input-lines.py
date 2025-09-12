import sys
import re

def main():
    # Check command line args
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = "input.txt"

    # Regex to match the javascript line
    pattern = re.compile(r"javascript:loadYoutube2\('.*?'\);")

    # Replacement HTML snippet
    replacement = (
        '<li class="svg-item"><img class="svg-icon" src="chetiya.svg">'
        '<button class="unstyled-button" onclick="loadYoutube2(\'iNbW0UjKlf0\')">'
        '01. වෙරඤ‍්ජකණ‍්ඩො (45min.), 2p</button>'
        '<button class="unstyled-button" onclick="sharePage(\'iNbW0UjKlf0\')">'
        '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" '
        'viewBox="0 0 24 24"><path fill="currentColor" fill-rule="evenodd" '
        'd="M13.803 5.333c0-1.84 1.5-3.333 3.348-3.333A3.34 3.34 0 0 1 20.5 5.333c0 '
        '1.841-1.5 3.334-3.349 3.334-.933 0-1.777-.381-2.384-.994l-4.635 3.156a3.34 '
        '3.34 0 0 1-.182 1.917l5.082 3.34a3.35 3.35 0 0 1 2.12-.753 3.34 3.34 0 0 '
        '1 3.348 3.334C20.5 20.507 19 22 17.151 22a3.34 3.34 0 0 1-3.348-3.333c0-.483.103-.942.289-1.356L9.05 '
        '14a3.35 3.35 0 0 1-2.202.821A3.34 3.34 0 0 1 3.5 11.487a3.34 3.34 0 0 1 '
        '3.348-3.333c1.064 0 2.01.493 2.623 1.261l4.493-3.059a3.3 3.3 0 0 '
        '1-.161-1.023" clip-rule="evenodd"/></svg></button></li>'
    )

    # Process the file
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        if pattern.search(line):
            new_lines.append(replacement + "\n")
        else:
            new_lines.append(line)

    # Write output
    with open(output_file, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    print(f"Done — wrote output to {output_file}")

if __name__ == "__main__":
    main()
