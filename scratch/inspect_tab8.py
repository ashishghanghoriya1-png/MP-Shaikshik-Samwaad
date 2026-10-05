import re

with open('RSK_Master_CLSS_Executive_Dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'(<section[^>]+id=["\']tab-governance["\'].*?</section>)', html, re.DOTALL)
if m:
    with open('tab_gov_section.html', 'w', encoding='utf-8') as out:
        out.write(m.group(1))
    print("Saved tab_gov_section.html (len:", len(m.group(1)), ")")
else:
    print("Section tab-governance not found!")
