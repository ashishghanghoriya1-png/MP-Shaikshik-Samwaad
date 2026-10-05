import io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('RSK_Master_CLSS_Executive_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_init_d360 = text.find('function initDistrict360()')
pos_upd_comp = text.find('function populateComparisonDropdowns()', pos_init_d360)

print(f"initDistrict360 to populateComparisonDropdowns in master: {pos_init_d360} to {pos_upd_comp}")
print("--- Code to replace ---")
print(text[pos_init_d360:pos_init_d360+400])
print("...")
print(text[pos_upd_comp-300:pos_upd_comp])
