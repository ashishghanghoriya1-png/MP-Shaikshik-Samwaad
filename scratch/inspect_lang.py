import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Master Dashboard for CLSS\RSK_Master_CLSS_Executive_Studio_Enhanced.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect translations en and hi
en_idx = html.find("en: {")
hi_idx = html.find("hi: {")
print("en starts at:", en_idx)
print("hi starts at:", hi_idx)

# Let's see how setLanguage handles tab elements or elements by ID
lang_fn = re.search(r'function setLanguage\(.*?\)\s*\{', html)
if lang_fn:
    print("setLanguage fn snippet:\n", html[lang_fn.start():lang_fn.start()+800])
