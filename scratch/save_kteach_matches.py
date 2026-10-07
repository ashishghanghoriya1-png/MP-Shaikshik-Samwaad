html = open('index.html', encoding='utf-8').read()

import re

out = []
for m in re.finditer(r'kTeach(?:Desc|Badge)?\.(?:innerText|innerHTML)\s*=', html):
    p = m.start()
    out.append('=== MATCH ===')
    out.append(html[max(0, p-150):min(len(html), p+350)])

open('scratch/kteach_matches.txt', 'w', encoding='utf-8').write('\n'.join(out))
print('Saved matches to scratch/kteach_matches.txt')
