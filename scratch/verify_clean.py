import re

with open('RSK_Master_CLSS_Executive_Dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("Sheet2 / Sheet 2 occurrences:", html.count("Sheet2") + html.count("Sheet 2"))
print("Field Bottlenecks occurrences:", len(re.findall(r'Field Bottlenecks', html, re.IGNORECASE)))
print("Strategic Intelligence occurrences:", len(re.findall(r'Strategic Intelligence', html, re.IGNORECASE)))
print("Total characters in HTML:", len(html))
