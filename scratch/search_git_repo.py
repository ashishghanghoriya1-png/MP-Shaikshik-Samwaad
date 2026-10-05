import os, glob, re

# Search recent files or configs for github.com
patterns = [
    r'c:\Users\Peepul\.gitconfig',
    r'c:\Users\Peepul\.bash_history',
    r'c:\Users\Peepul\AppData\Roaming\Git\*',
    r'c:\Users\Peepul\*.md',
    r'c:\Users\Peepul\*.txt'
]

found = []
for p in patterns:
    for fpath in glob.glob(p):
        if os.path.isfile(fpath):
            try:
                with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
                    for line in f:
                        if 'github.com' in line or 'git@' in line or 'ashishghanghoriya' in line:
                            found.append((fpath, line.strip()))
            except Exception as e:
                pass

print(f"Found {len(found)} references:")
for fpath, line in found[:20]:
    print(f"{fpath}: {line}")
