import io, sys, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('RSK_Master_CLSS_Executive_Studio_Enhanced.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_start = text.find('id="tab-d360"')
pos_end = text.find('</section>', pos_start)
tab3_html = text[pos_start:pos_end]

ids = re.findall(r'id=["\']([^"\']+)["\']', tab3_html)
print(f"Total IDs in Tab 3 HTML: {len(ids)}")
for i in ids:
    print(f"  • #{i}")
