import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Master Dashboard for CLSS\RSK_Master_CLSS_Executive_Studio_Enhanced.html', 'r', encoding='utf-8') as f:
    html = f.read()

res_start = html.find('id="tab-research"')
print("tab-research starts around index:", res_start)

# Find the next closing section or start of script
snippet = html[res_start:res_start+40000]
# Look for </section> or <script
script_pos = html.find('<script', res_start)
print("Next script tag is at:", script_pos)

# Let's inspect the last 500 chars before <script
print("Chars before script:\n", html[script_pos-500:script_pos])
