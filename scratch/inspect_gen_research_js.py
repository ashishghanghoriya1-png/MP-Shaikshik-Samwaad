import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('RSK_Master_CLSS_Executive_Studio_Enhanced.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('function initResearchTab')
print("Snippet around initResearchTab in generated HTML:")
print(text[pos:pos+1000])

pos2 = text.find('function toggleAbstractLang')
print("\nSnippet around toggleAbstractLang in generated HTML:")
print(text[pos2:pos2+1000])
