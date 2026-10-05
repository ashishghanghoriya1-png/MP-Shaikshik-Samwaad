import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('RSK_Master_CLSS_Executive_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find("tabId === 'tab-governance'")
print("Snippet around tab-governance in master:")
print(text[pos:pos+400])
