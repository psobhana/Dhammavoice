# Read lines from input.txt
with open('input.txt', 'r', encoding='utf-8') as f1:
    lines1 = f1.read().splitlines()

# Read lines from input2.txt
with open('input2.txt', 'r', encoding='utf-8') as f2:
    lines2 = f2.read().splitlines()

# Join corresponding lines and write to words.txt
with open('words.txt', 'w', encoding='utf-8') as output:
    for line1, line2 in zip(lines1, lines2):
        output.write(f"{line1} {line2}\n")
