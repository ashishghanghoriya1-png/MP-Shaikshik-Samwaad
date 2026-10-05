import re

with open(r'c:\Master Dashboard for CLSS\RSK_Master_CLSS_Executive_Studio_Enhanced.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Check activateTab
tab_fn_match = re.search(r'function activateTab\(tabId, el\)\s*\{', html)
if tab_fn_match:
    print("Found activateTab")
    fn_body = html[tab_fn_match.start():tab_fn_match.start()+600]
    print(fn_body)
