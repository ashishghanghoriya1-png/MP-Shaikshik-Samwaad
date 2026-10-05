import re

with open(r'c:\Master Dashboard for CLSS\RSK_Master_CLSS_Executive_Studio_Enhanced.html', 'r', encoding='utf-8') as f:
    html = f.read(50000)

lines = html.splitlines()
for i, line in enumerate(lines[:300]):
    if any(k in line.lower() for k in ['nav', 'tab', 'section', 'button', 'sidebar']):
        print(f"L{i+1}: {line.strip()[:120]}")
