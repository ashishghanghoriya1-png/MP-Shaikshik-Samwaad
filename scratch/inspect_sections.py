import io
import sys
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('RSK_Master_CLSS_Executive_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'<section[^>]*id=["\'](tab-[^"\']+)["\']', text):
    print('Found section:', m.group(1), 'at pos', m.start())

print("\n--- Searching for tab-insights end ---")
m = re.search(r'<section[^>]*id=["\']tab-insights["\'].*?</section>', text, re.DOTALL)
if m:
    print("Found tab-insights section length:", len(m.group(0)))
    print("tab-insights snippet:", m.group(0)[:200], "...", m.group(0)[-200:])
