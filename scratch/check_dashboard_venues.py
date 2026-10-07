
import re

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

print('index.html size:', len(text))
# Check if 2,920 or 2,972 or 2,872 is in text
for target in ['2,872', '2,822', '2,920', '2,972', '2,861', '2,874']:
    c = text.count(target)
    print(f'{target}: {c} occurrences')
