import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Master Dashboard for CLSS\RSK_Master_CLSS_Executive_Studio_Enhanced.html', 'r', encoding='utf-8') as f:
    html = f.read()

body_start = html.find('<body')
body_snippet = html[body_start:body_start+15000]

import re
# Find all buttons or slicers or tab links
matches = re.findall(r'(<(?:nav|div|button|a)[^>]*class="[^"]*(?:tab|nav|view|slicer)[^"]*"[^>]*>.*?</(?:nav|div|button|a)>)', body_snippet, re.DOTALL)
print(f"Matches found: {len(matches)}")
for m in matches[:20]:
    print("MATCH:", m[:150])
