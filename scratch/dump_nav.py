with open('RSK_Master_CLSS_Executive_Dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('studio-nav')
idx2 = html.find('</nav>', idx)

with open('scratch/nav_dump.html', 'w', encoding='utf-8') as out:
    out.write(html[idx:idx2+6])

print("Written scratch/nav_dump.html")
