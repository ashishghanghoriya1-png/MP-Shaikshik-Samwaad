import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Master Dashboard for CLSS\RSK_Master_CLSS_Executive_Studio_Enhanced.html', 'r', encoding='utf-8') as f:
    html = f.read()

res_match = [m.start() for m in re.finditer(r'navTabResearch', html)]
print("Occurrences of navTabResearch:", res_match)
for pos in res_match:
    print("Snippet around pos:\n", html[pos-50:pos+200])
