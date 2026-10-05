import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('build_enhanced_studio.py', 'r', encoding='utf-8') as f:
    text = f.read()

print("initResearchTab in build_enhanced_studio.py:", 'initResearchTab' in text)
print("tab-research in build_enhanced_studio.py:", 'tab-research' in text)
print("navTabResearch in build_enhanced_studio.py:", 'navTabResearch' in text)
