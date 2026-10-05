import io, sys, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('RSK_Master_CLSS_Executive_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('surveys')
while pos != -1:
    print("Found 'surveys' at pos", pos, ":", text[max(0, pos-40):min(len(text), pos+150)])
    pos = text.find('surveys', pos+1)
    if pos > 300000: break
