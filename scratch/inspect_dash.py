import os, re, sys

dash_path = r'c:\Master Dashboard for CLSS\RSK_Master_CLSS_Executive_Studio_Enhanced.html'
with open(dash_path, 'r', encoding='utf-8') as f:
    html = f.read()

print("HTML Length:", len(html))

# Find nav items
nav_matches = re.findall(r'<button[^>]*onclick="[^"]*showTab\([^"]*\)[^"]*"[^>]*>.*?</button>', html, re.I | re.DOTALL)
if not nav_matches:
    nav_matches = re.findall(r'<button[^>]*data-tab="[^"]*"[^>]*>.*?</button>', html, re.I | re.DOTALL)
if not nav_matches:
    nav_matches = re.findall(r'<button[^>]*class="[^"]*tab[^"]*"[^>]*>.*?</button>', html, re.I | re.DOTALL)
if not nav_matches:
    nav_matches = re.findall(r'<div[^>]*class="[^"]*tab-content[^"]*"[^>]*id="([^"]*)"', html, re.I)

print("Found tab elements/ids:")
for m in nav_matches:
    print(m)

# Find sections or tabs by id
tab_divs = re.findall(r'<div[^>]*id="tab-([^"]+)"', html)
print("\nTab Div IDs (tab-*):", tab_divs)

# Also check any other tab IDs
all_tab_divs = re.findall(r'<div[^>]*class="[^"]*tab-pane[^"]*"[^>]*id="([^"]+)"', html)
print("Tab Panes:", all_tab_divs)
