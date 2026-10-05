import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('build_enhanced_studio.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('tab-insights')
while pos != -1:
    print("--- tab-insights snippet at pos", pos, "---")
    print(text[pos:pos+250])
    pos = text.find('tab-insights', pos+1)
