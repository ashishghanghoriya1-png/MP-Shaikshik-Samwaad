html = open('index.html', encoding='utf-8').read()

import re

for m in re.finditer(r'kpiTeachersDesc', html):
    p = m.start()
    print('=== kpiTeachersDesc CONTEXT ===')
    print(html[max(0, p-200):min(len(html), p+600)])
