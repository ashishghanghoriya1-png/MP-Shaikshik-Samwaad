import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('build_enhanced_studio.py', 'r', encoding='utf-8') as f:
    text = f.read()

print("initResearchTab in build_enhanced_studio.py:", text.find('function initResearchTab'))
print("Where is initResearchTab in build_enhanced_studio.py?")
pos = 0
while True:
    p = text.find('initResearchTab', pos)
    if p == -1: break
    print("Found at pos", p, ":", text[max(0, p-40):min(len(text), p+60)])
    pos = p + 1
