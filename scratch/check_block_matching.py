import io, sys, json

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('RSK_Master_CLSS_Executive_Studio_Enhanced.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_dp = text.find('const dataPackage =')
pos_dp_end = text.find(';\n', pos_dp)
data = json.loads(text[pos_dp+20:pos_dp_end].strip())

blockSummary = data.get('blockSummary', [])
districtSummary = data.get('districtSummary', [])

print(f"Total blocks in blockSummary: {len(blockSummary)}")
sample_blocks = blockSummary[:5]
for b in sample_blocks:
    print("Sample block:", b)

print("\nDistricts in districtSummary:")
d_names = [d.get('district') for d in districtSummary[:5]]
print(d_names)

print("\nMatching blocks for district 'Agar Malwa':")
agar_blocks = [b for b in blockSummary if b.get('district') == 'Agar Malwa']
print(f"Found {len(agar_blocks)} blocks for 'Agar Malwa':", [b.get('block') for b in agar_blocks])

print("\nMatching blocks for first 10 districts in districtSummary:")
for d in districtSummary[:10]:
    dn = d.get('district')
    blks = [b for b in blockSummary if str(b.get('district')).strip().lower() == str(dn).strip().lower()]
    print(f"District '{dn}': {len(blks)} blocks found in blockSummary")
