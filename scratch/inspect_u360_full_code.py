import io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('RSK_Master_CLSS_Executive_Studio_Enhanced.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('function updateDistrict360View()')
pos_end = text.find('function updateDistrictComparison()', pos)
print("--- FULL updateDistrict360View in JS ---")
print(text[pos:pos_end])
