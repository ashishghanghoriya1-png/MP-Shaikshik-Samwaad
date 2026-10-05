with open(r'C:\My Files Work\CLSS RF BI\RSK_Executive_BI_ProMax.html', 'r', encoding='utf-8') as f:
    tpl = f.read()

idx = tpl.find('id="tab-governance"')
idx2 = tpl.find('</main>', idx)

with open('scratch/template_tab8.html', 'w', encoding='utf-8') as out:
    out.write(tpl[idx-50:idx2])

print("Written scratch/template_tab8.html")
