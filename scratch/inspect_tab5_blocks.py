import io, sys, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('RSK_Master_CLSS_Executive_Studio_Enhanced.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_blocks = text.find('id="tab-blocks"')
print("Tab 5 (Blocks) HTML snippet:")
print(text[pos_blocks:pos_blocks+1200])

print("\n--- Searching for all occurrences of 'blockDistrictSelect' or 'initBlockDirectory' ---")
pos = text.find('function initBlockDirectory')
if pos != -1:
    print(text[pos:pos+1000])
else:
    print("initBlockDirectory not found")
