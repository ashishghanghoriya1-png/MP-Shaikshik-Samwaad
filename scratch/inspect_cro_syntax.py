import io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('build_enhanced_studio.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('id="croPanelHeading"')
print("Found croPanelHeading at:", pos)
print("Context:")
print(text[max(0, pos-200):min(len(text), pos+300)])
