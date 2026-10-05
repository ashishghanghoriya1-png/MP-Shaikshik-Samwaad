import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Master Dashboard for CLSS\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

lines = html.splitlines()
print(f"Total lines: {len(lines)}")
for i, l in enumerate(lines):
    if 'tolowercase' in l.lower():
        print(f"Line {i+1}: {l.strip()[:140]}")
