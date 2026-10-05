import re

html = open('index.html', encoding='utf-8').read()
kpi_ids = re.findall(r'id=["\']([^"\']*kpi[^"\']*)["\']', html, re.IGNORECASE)
print('KPI IDs found in index.html:', sorted(list(set(kpi_ids))))

filters = re.findall(r'id=["\']([^"\']*(?:filter|select|search|btn|cycle|lang)[^"\']*)["\']', html, re.IGNORECASE)
print('Filter IDs found:', sorted(list(set(filters)))[:25])
