import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Master Dashboard for CLSS\RSK_Master_CLSS_Executive_Studio_Enhanced.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find nav buttons
nav_match = re.search(r'<nav class="studio-nav[^"]*">.*?</nav>', html, re.DOTALL)
if nav_match:
    print("NAV BLOCK:\n", nav_match.group(0))

# Find tab-research container and its end
res_match = re.search(r'<div[^>]*id="tab-research"[^>]*>', html)
if res_match:
    start_pos = res_match.start()
    print("\nFound tab-research at:", start_pos)
    # let's see what follows tab-research
    print("Snippet around tab-research (first 400 chars):\n", html[start_pos:start_pos+400])

# Find script translations or activateTab
tab_fn_match = re.search(r'function activateTab\(.*?\)\s*\{', html)
if tab_fn_match:
    print("\nFound activateTab at:", tab_fn_match.start())
    print("activateTab snippet:\n", html[tab_fn_match.start():tab_fn_match.start()+600])

# Find translation dict
trans_match = re.search(r'const translations\s*=\s*\{', html)
if trans_match:
    print("\nFound translations at:", trans_match.start())
    print("translations snippet:\n", html[trans_match.start():trans_match.start()+600])
