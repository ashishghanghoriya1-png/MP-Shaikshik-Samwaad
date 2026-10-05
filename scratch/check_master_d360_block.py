import io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('RSK_Master_CLSS_Executive_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_start = text.find('function initDistrict360()')
pos_end = text.find('// 3. District League', pos_start)

print(f"In master HTML: initDistrict360 at {pos_start}, District League at {pos_end}")
print("--- Code snippet to replace in master ---")
print(text[pos_start:pos_start+300])
print("...")
print(text[pos_end-300:pos_end])
