import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Master Dashboard for CLSS\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find last 100 lines of index.html
lines = html.splitlines()
print(f"Total lines: {len(lines)}")
for i, l in enumerate(lines[-100:]):
    print(f"L{len(lines)-100+i+1}: {l[:120]}")
