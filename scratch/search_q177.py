import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Master Dashboard for CLSS\RSK_Master_CLSS_Executive_Studio_Enhanced.html', 'r', encoding='utf-8') as f:
    html = f.read()

patterns = ['18,493', '(0 teachers)', 'hands-on craft', 'cognitive reflection', 'experiential cycle', 'Q177', 'Q178', 'Q179']
for p in patterns:
    matches = [m.start() for m in re.finditer(re.escape(p), html, re.IGNORECASE)]
    print(f"\nPattern '{p}': found {len(matches)} occurrences")
    for pos in matches[:4]:
        print(f"  Snippet at {pos}:\n    ", html[max(0, pos-100):min(len(html), pos+200)].replace('\n', ' '))
