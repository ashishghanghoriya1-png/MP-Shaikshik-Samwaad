import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Master Dashboard for CLSS\RSK_Master_CLSS_Executive_Studio_Enhanced.html', 'r', encoding='utf-8') as f:
    html = f.read()

body_start = html.find('<body')
print("Body starts at:", body_start)
if body_start != -1:
    body_snippet = html[body_start:body_start+4000]
    print("Body snippet:\n", body_snippet)
