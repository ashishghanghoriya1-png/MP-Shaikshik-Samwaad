import subprocess, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

old_index = subprocess.check_output(['git', 'show', '19b3486:index.html'], cwd=r'c:\Master Dashboard for CLSS', encoding='utf-8', errors='ignore')
with open(r'c:\Master Dashboard for CLSS\index.html', 'r', encoding='utf-8') as f:
    new_index = f.read()

print(f"Old index size: {len(old_index):,} chars")
print(f"New index size: {len(new_index):,} chars")

old_tabs = re.findall(r'<button class="nav-item[^"]*"[^>]*>.*?</button>', old_index)
new_tabs = re.findall(r'<button class="nav-item[^"]*"[^>]*>.*?</button>', new_index)

print("\nOld tabs count:", len(old_tabs))
for t in old_tabs:
    print("  OLD:", t.strip())

print("\nNew tabs count:", len(new_tabs))
for t in new_tabs:
    print("  NEW:", t.strip())

old_sections = re.findall(r'<section[^>]*id="([^"]+)"', old_index)
new_sections = re.findall(r'<section[^>]*id="([^"]+)"', new_index)

print("\nOld sections:", old_sections)
print("New sections:", new_sections)
missing_sections = set(old_sections) - set(new_sections)
print("Missing sections in new:", missing_sections)

# Check differences in line diff
diff_lines = subprocess.check_output(['git', 'diff', '19b3486:index.html', 'index.html'], cwd=r'c:\Master Dashboard for CLSS', encoding='utf-8', errors='ignore')
print(f"\nDiff line count: {len(diff_lines.splitlines()):,}")
deleted_lines = [l for l in diff_lines.splitlines() if l.startswith('-') and not l.startswith('---')]
print(f"Total deleted lines: {len(deleted_lines)}")
for dl in deleted_lines[:20]:
    print("  DEL:", dl[:120])
