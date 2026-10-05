with open('RSK_Master_CLSS_Executive_Dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('id="tab-governance"')
if idx == -1:
    idx = html.find("id='tab-governance'")

print("Found index:", idx)
with open('scratch/tab8_dump.html', 'w', encoding='utf-8') as out:
    out.write(html[idx-100:idx+3000])

print("Written scratch/tab8_dump.html successfully")
