with open('c:/Master Dashboard for CLSS/RSK_Master_CLSS_Executive_Dashboard.html', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="tab-governance"')
if idx != -1:
    with open('c:/Master Dashboard for CLSS/scratch/tab_gov_section.html', 'w', encoding='utf-8') as f:
        f.write(text[idx-50:idx+3500])
    print('Wrote tab_gov_section.html!')
