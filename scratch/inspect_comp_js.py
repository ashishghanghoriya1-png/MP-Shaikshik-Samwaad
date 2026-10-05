import io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('RSK_Master_CLSS_Executive_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos1 = text.find('function updateDistrictComparison()')
pos2 = text.find('// 3. District League', pos1)

print(text[pos1:pos2])
