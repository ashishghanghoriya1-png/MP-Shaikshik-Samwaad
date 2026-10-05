import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('RSK_Master_CLSS_Executive_Dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_q = text.find('id="tab-questions"')
print("Tab 6 HTML snippet:")
print(text[pos_q:pos_q+1200])

pos_js_q = text.find('function renderQuestionBankActive')
if pos_js_q != -1:
    print("\nrenderQuestionBankActive in JS:")
    print(text[pos_js_q:pos_js_q+1200])
else:
    print("\nSearching for question bank JS...")
    pos_alt = text.find('questionBank')
    print(text[pos_alt:pos_alt+1000])
