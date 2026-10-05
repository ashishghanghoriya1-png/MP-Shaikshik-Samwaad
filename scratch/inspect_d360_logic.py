import io, sys, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('RSK_Master_CLSS_Executive_Studio_Enhanced.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('function updateDistrict360View()')
print("--- updateDistrict360View() in Enhanced HTML ---")
print(text[pos:pos+4000])

pos_block_ch = text.find('function onD360BlockChange()')
print("\n--- onD360BlockChange() in Enhanced HTML ---")
print(text[pos_block_ch:pos_block_ch+1000])
