import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:/My Files Work/CLSS RF BI/RSK_Executive_BI_ProMax.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("--- SLICER CSS RULES ---")
for m in re.finditer(r'(\.[a-zA-Z0-9_-]*slicer[a-zA-Z0-9_ -]*\s*\{[^}]+\})', html):
    print(m.group(1))
    print('-'*40)

print("\n--- SLICER HTML CONTAINERS (Header / Ribbon) ---")
# find where slicer controls are placed in the header/ribbon
for m in re.finditer(r'(<div[^>]*class="[^"]*(?:slicer|filter-bar|control-bar|ribbon)[^"]*"[\s\S]*?</nav>)', html):
    print(m.group(1)[:2500])
