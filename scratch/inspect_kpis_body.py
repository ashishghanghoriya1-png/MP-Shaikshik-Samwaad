import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Master Dashboard for CLSS\RSK_Master_CLSS_Executive_Studio_Enhanced.html', 'r', encoding='utf-8') as f:
    html = f.read()

kpis_fn = re.search(r'function updateKPIs\(.*?\)\s*\{', html)
if kpis_fn:
    body = html[kpis_fn.start():kpis_fn.start()+3500]
    print(body)
