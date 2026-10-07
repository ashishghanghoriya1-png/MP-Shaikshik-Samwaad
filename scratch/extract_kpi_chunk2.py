html = open('index.html', encoding='utf-8').read()

pos = html.find('const clssTeache')
print('Found at pos:', pos)
open('scratch/kpi_chunk2.txt', 'w', encoding='utf-8').write(html[pos:pos+2000])
