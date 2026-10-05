import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Master Dashboard for CLSS\RSK_Master_CLSS_Executive_Studio_Enhanced.html', 'r', encoding='utf-8') as f:
    html = f.read()

res_start = html.find('id="tab-research"')
section_end = html.find('</section>', res_start)
print("tab-research section ends at:", section_end)
print("Snippet around section end:\n", html[section_end-200:section_end+200])
