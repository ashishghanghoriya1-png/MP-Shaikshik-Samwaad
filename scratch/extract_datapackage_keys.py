import io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('RSK_Master_CLSS_Executive_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_dp = text.find('const dataPackage =')
print("dataPackage start at:", pos_dp)
pos_dp_end = text.find(';\n', pos_dp)
print("dataPackage length:", pos_dp_end - pos_dp)

# Extract keys
import json
dp_raw = text[pos_dp+20:pos_dp_end].strip()
print("First 200 chars of dataPackage:", dp_raw[:200])
print("Last 200 chars of dataPackage:", dp_raw[-200:])
