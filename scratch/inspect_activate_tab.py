import io
import sys
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('RSK_Master_CLSS_Executive_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'function activateTab\(.*?\n    \}', text, re.DOTALL)
if m:
    print("activateTab definition:\n", m.group(0))
else:
    print("Could not find activateTab with simple regex, searching broader...")
    pos = text.find('function activateTab')
    print(text[pos:pos+1500])
