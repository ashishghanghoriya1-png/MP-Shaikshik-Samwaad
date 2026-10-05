import re

with open('RSK_Master_CLSS_Executive_Dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

for m in re.finditer(r'id=["\'](tab-[^"\']+)["\']', html):
    print("Found tab ID:", m.group(1), "at pos:", m.start())

for m in re.finditer(r'tab-governance', html):
    print("Found string tab-governance at pos:", m.start())
    print("Context:", repr(html[max(0, m.start()-50):min(len(html), m.start()+150)]))
