html = open('index.html', encoding='utf-8').read()

import re

out = []
for m in re.finditer(r'btnCycle(?:Sep|Aug|Consolidated|Select)', html):
    p = m.start()
    out.append('=== CYCLE BTN CONTEXT ===')
    out.append(html[max(0, p-100):min(len(html), p+400)])

open('scratch/cycle_btn_matches.txt', 'w', encoding='utf-8').write('\n'.join(out))
print('Saved to scratch/cycle_btn_matches.txt')
