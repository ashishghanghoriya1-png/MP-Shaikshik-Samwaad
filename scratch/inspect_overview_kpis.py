import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Master Dashboard for CLSS\RSK_Master_CLSS_Executive_Studio_Enhanced.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Check Overview KPI figures
ov_start = html.find('id="tab-overview"')
ov_end = html.find('</section>', ov_start)
ov_html = html[ov_start:ov_end]

print("Overview section snippet:\n", ov_html[:3000])

# Check JS functions that populate overview or month slicer
slicer_fn = re.search(r'function setMonthSlicer\(.*?\)\s*\{', html)
if slicer_fn:
    print("\nsetMonthSlicer snippet:\n", html[slicer_fn.start():slicer_fn.start()+800])
