html = open('index.html', encoding='utf-8').read()

pos = html.find('if (kTeach)')
if pos == -1:
    pos = html.find('kTeach')
print('Found at pos:', pos)
open('scratch/kpi_chunk3.txt', 'w', encoding='utf-8').write(html[pos:pos+2000])
