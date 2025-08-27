import re
import sys

def update_sharefile(filename):
    # Read all lines
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    updated_lines = []
    for line in lines:
        # Look for href="SOME_URL.pdf"
        match = re.search(r'href="([^"]+\.pdf)"', line)
        if match:
            pdf_url = match.group(1)
            # Replace inside shareFile('...')
            line = re.sub(r"shareFile\('([^']*)'\)", f"shareFile('{pdf_url}')", line)
        updated_lines.append(line)

    # Write back to file (overwrite)
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(updated_lines)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python update_sharefile.py <filename>")
        sys.exit(1)

    update_sharefile(sys.argv[1])
    print("File updated successfully!")
