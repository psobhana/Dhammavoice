#!/usr/bin/env python3
import argparse
import re
from pathlib import Path

PREFIX_RE = re.compile(r"^\s*\d+\.\s*")

def clean_line(line: str) -> str:
    newline = "\n" if line.endswith("\n") else ""
    core = line[:-1] if newline else line
    
    core = core.lstrip()
    core = PREFIX_RE.sub("", core)
    core = core.lstrip()
    
    return core + newline

def main():
    parser = argparse.ArgumentParser(
        description="Remove leading 'NN.' prefixes and leading spaces from every line."
    )
    parser.add_argument("input_file", help="Path to input text file")
    args = parser.parse_args()
    
    in_path = Path(args.input_file)
    
    # Read input as UTF-8
    with in_path.open("r", encoding="utf-8") as f:
        lines = f.readlines()
    
    # Clean lines
    cleaned = [clean_line(line) for line in lines]
    
    # Write to words.txt
    with open("words.txt", "w", encoding="utf-8", newline="") as out:
        out.writelines(cleaned)
    
    print(f"Output written to words.txt")

if __name__ == "__main__":
    main()
