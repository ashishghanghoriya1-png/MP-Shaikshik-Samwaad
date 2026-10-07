html = open('index.html', encoding='utf-8').read()

pos = html.find('const kTeach = document.getElementById(\'kpiTeachers\');')
print('Found at pos:', pos)
start = max(0, pos - 500)
end = min(len(html), pos + 2500)
open('scratch/kpi_update_fn.txt', 'w', encoding='utf-8').write(html[start:end])
print('Wrote to scratch/kpi_update_fn.txt')
