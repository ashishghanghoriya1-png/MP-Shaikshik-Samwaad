import io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('build_enhanced_studio.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos_start = text.find('function initDistrict360()')
pos_end = text.find('function initDistrictLeague()')
print(f"initDistrict360 to initDistrictLeague boundary in build_enhanced_studio.py: {pos_start} to {pos_end}")
if pos_start != -1 and pos_end != -1:
    print("Found block snippet in build_enhanced_studio.py:")
    print(text[pos_start:pos_start+300])
    print("...")
    print(text[pos_end-300:pos_end])
else:
    print("Checking where updateDistrict360View is located...")
    p1 = text.find('updateDistrict360View')
    while p1 != -1:
        print("Found at:", p1, text[p1:p1+100])
        p1 = text.find('updateDistrict360View', p1+1)
