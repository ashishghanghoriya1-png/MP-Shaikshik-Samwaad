import io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('RSK_Master_CLSS_Executive_Studio_Enhanced.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_start = text.find('id="tab-d360"')
pos_end = text.find('</section>', pos_start)
print("--- FULL TAB-D360 HTML MARKUP ---")
print(text[pos_start:pos_end+10])
