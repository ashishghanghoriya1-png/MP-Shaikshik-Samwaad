import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:/My Files Work/CLSS RF BI/RSK_Executive_BI_ProMax.html', 'r', encoding='utf-8') as f:
    html = f.read()

matches = [m.start() for m in re.finditer(r'activeRole', html)]
print(f"Total occurrences of activeRole: {len(matches)}")
for idx, pos in enumerate(matches):
    start = max(0, pos - 50)
    end = min(len(html), pos + 100)
    print(f"[{idx+1}] {html[start:end].strip().replace('\n', ' ')}")
