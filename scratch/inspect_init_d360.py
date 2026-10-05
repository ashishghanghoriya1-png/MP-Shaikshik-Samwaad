import io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('RSK_Master_CLSS_Executive_Studio_Enhanced.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('function initDistrict360()')
if pos == -1:
    pos = text.find('initDistrict360')
print("initDistrict360 context:")
print(text[pos:pos+1500])

pos_pdd = text.find('function populateDistrictDropdowns()')
if pos_pdd != -1:
    print("\npopulateDistrictDropdowns:")
    print(text[pos_pdd:pos_pdd+1200])
