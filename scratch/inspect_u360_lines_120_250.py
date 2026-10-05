import io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('RSK_Master_CLSS_Executive_Studio_Enhanced.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('function updateDistrict360View()')
pos_end = text.find('function updateDistrictComparison()', pos)
full_u360 = text[pos:pos_end]

lines = full_u360.splitlines()
for i in range(120, min(250, len(lines))):
    print(f"{i+1:3d}: {lines[i]}")
