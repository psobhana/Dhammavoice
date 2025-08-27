import re
import sys

def update_share_ids(filename):
    # Read the file
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    updated_lines = []
    for line in lines:
        # Look for loadYoutube2('VIDEO_ID')
        match = re.search(r"loadYoutube2\('([^']+)'\)", line)
        if match:
            video_id = match.group(1)
            # Replace inside sharePage('...')
            line = re.sub(r"sharePage\('([^']*)'\)", f"sharePage('{video_id}')", line)
        updated_lines.append(line)

    # Write back to file (overwrite)
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(updated_lines)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python update_share.py <filename>")
        sys.exit(1)

    update_share_ids(sys.argv[1])
    print("File updated successfully!")
