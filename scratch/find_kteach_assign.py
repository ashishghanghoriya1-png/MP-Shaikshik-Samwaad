html = open('index.html', encoding='utf-8').read()

import re

for m in re.finditer(r'kTeach(?:Desc|Badge)?\.(?:innerText|innerHTML)\s*=', html):
    p = m.start()
    print('=== MATCH ===')
    print(html[max(0, p-100):min(len(html), p+300)])
