import io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('RSK_Master_CLSS_Executive_Studio_Enhanced.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_sum = text.find('id="d360SumContainer"')
pos_bif = text.find('id="d360BifurcationContainer"')

print("--- d360SumContainer snippet ---")
print(text[pos_sum:pos_sum+800])

print("\n--- d360BifurcationContainer snippet ---")
print(text[pos_bif:pos_bif+1200])
