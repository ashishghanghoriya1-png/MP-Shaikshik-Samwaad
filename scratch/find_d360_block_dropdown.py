import io, sys, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('RSK_Master_CLSS_Executive_Studio_Enhanced.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("Occurrences of 'd360BlockDropdown':")
pos = 0
while True:
    p = text.find('d360BlockDropdown', pos)
    if p == -1: break
    print(f"--- at pos {p} ---")
    print(text[max(0, p-60):min(len(text), p+200)])
    pos = p + 1

print("\nOccurrences of 'populateDistrictDropdowns' or 'updateDistrict360View':")
pos = 0
while True:
    p = text.find('updateDistrict360View', pos)
    if p == -1: break
    print(f"--- at pos {p} ---")
    print(text[max(0, p-60):min(len(text), p+200)])
    pos = p + 1
