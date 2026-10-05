import io, sys, json, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('RSK_Master_CLSS_Executive_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const dataPackage\s*=\s*(\{.*?\});\s*\n', text, re.DOTALL)
if m:
    # let's see surveys in dataPackage
    print("Found dataPackage definition")
    pos_surveys = text.find('surveys:')
    print("Surveys snippet in dataPackage:")
    print(text[pos_surveys:pos_surveys+1000])
else:
    print("Could not regex dataPackage")
