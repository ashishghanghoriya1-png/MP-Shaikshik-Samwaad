with open(r'c:\Master Dashboard for CLSS\scratch\main_script.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
for i in range(max(0, 6460), min(len(lines), 6475)):
    print(f"L{i+1}: {lines[i].strip()}")
