import io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('RSK_Master_CLSS_Executive_Studio_Enhanced.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('function updateDistrict360View()')
pos_end = text.find('function populateComparisonDropdowns()', pos)
full_u360 = text[pos:pos_end]

lines = full_u360.splitlines()
print(f"Total lines in updateDistrict360View: {len(lines)}")
for i in range(0, min(120, len(lines))):
    print(f"{i+1:3d}: {lines[i]}")
