import re

with open('c:/Master Dashboard for CLSS/RSK_Master_CLSS_Executive_Dashboard.html', encoding='utf-8') as f:
    text = f.read()

canvases = re.findall(r'<canvas[^>]+id=["\']([^"\']+)["\']', text)
print('All Canvas IDs in HTML:', canvases)
