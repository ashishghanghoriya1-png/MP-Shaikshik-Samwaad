import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r"C:\My Files Work\CLSS RF BI\RSK_Executive_BI_ProMax.html", "r", encoding="utf-8") as f:
    text = f.read()

pos = text.find('id="kpiDistricts"')
if pos != -1:
    print(text[pos-100:pos+1600])
