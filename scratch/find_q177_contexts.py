import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Master Dashboard for CLSS\RSK_Master_CLSS_Executive_Studio_Enhanced.html', 'r', encoding='utf-8') as f:
    html = f.read()

matches = list(re.finditer(r'Q177', html))
print(f"Total occurrences of Q177: {len(matches)}")
for m in matches[:10]:
    start = max(0, m.start() - 150)
    end = min(len(html), m.end() + 250)
    print(f"\n--- Occurrence at {m.start()} ---")
    print(html[start:end])
