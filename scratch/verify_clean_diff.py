import subprocess, sys
sys.stdout.reconfigure(encoding='utf-8')

diff_output = subprocess.check_output(['git', 'diff', '19b3486..HEAD', '--', 'RSK_Master_CLSS_Executive_Studio_Enhanced.html'], cwd=r'c:\Master Dashboard for CLSS', encoding='utf-8', errors='ignore')

# Count insertions and deletions
lines = diff_output.splitlines()
plus_lines = [l for l in lines if l.startswith('+') and not l.startswith('+++')]
minus_lines = [l for l in lines if l.startswith('-') and not l.startswith('---')]

print(f"Total diff lines: {len(lines)}")
print(f"Total plus lines (added): {len(plus_lines)}")
print(f"Total minus lines (deleted): {len(minus_lines)}")

# Let's inspect any minus lines to make sure no original data was deleted or altered
print("\nMinus lines (should be minimal/none):")
for ml in minus_lines:
    print("  DEL:", ml[:120])
