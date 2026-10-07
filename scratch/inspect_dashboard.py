import re
import json

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

tabs = re.findall(r'data-tab="([^"]+)"[^>]*>([\s\S]*?)<', text)
print("Dashboard Navigation Tabs:")
seen = set()
for tab_id, label in tabs:
    clean_label = label.strip()
    if clean_label and tab_id not in seen:
        seen.add(tab_id)
        print(f" - [{tab_id}]: {clean_label}")

with open('dataPackage.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print("\n--- Dashboard Available Metrics & Modules ---")
for k, v in d.items():
    if isinstance(v, dict):
        print(f"Key: {k}, sub-keys: {list(v.keys())[:10]}")
    elif isinstance(v, list):
        print(f"Key: {k}, count: {len(v)}")
