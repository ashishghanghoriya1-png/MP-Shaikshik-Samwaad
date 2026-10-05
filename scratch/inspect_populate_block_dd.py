import io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('RSK_Master_CLSS_Executive_Studio_Enhanced.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('function populateD360BlockDropdown()')
print("populateD360BlockDropdown definition:")
print(text[pos:pos+1200])
