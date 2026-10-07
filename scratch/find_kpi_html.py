import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

workspace = r"C:\Users\Peepul\OneDrive - Absolute Return For Kids\Master Dashboard for CLSS - Copy"

with open(os.path.join(workspace, 'index.html'), 'r', encoding='utf-8') as f:
    text = f.read()

# Find the exact KPI block for District Orientation
idx = text.find("DISTRICT ORIENTATION PARTICIPANTS")
if idx != -1:
    print("=== KPI BLOCK IN INDEX.HTML ===")
    print(text[idx-200:idx+600])

# Find where 8,888 appears in index.html
idx2 = text.find("8,888")
if idx2 != -1:
    print("\n=== 8,888 BLOCK IN INDEX.HTML ===")
    print(text[idx2-200:idx2+300])
