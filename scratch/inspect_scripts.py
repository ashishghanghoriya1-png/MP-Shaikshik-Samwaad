import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Master Dashboard for CLSS\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all script tags
scripts = list(re.finditer(r'<script\b[^>]*>(.*?)</script>', html, re.DOTALL))
print(f"Total script blocks: {len(scripts)}")
for i, s in enumerate(scripts):
    print(f"Script #{i+1}: Start={s.start()}, End={s.end()}, Length={len(s.group(1)):,}")
    # check if renderCohortTab is inside this script
    if 'renderCohortTab' in s.group(1):
        print(f"  --> renderCohortTab is inside Script #{i+1}")

# Check if there is any syntax error in each script block by checking js
