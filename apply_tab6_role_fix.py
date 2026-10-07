"""
Fix Tab 6 Survey Question Bank Role Slicer filtering across all 4 dashboard targets.
Ensures checking (s.role || s.cadre) so selecting Teachers, Facilitators, or Monitors cleanly filters the 70 questions down to:
- Teachers: 26 Questions
- Facilitators: 24 Questions
- Monitors: 20 Questions
"""

import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

TARGET_FILES = [
    'index.html',
    'deploy/index.html',
    'RSK_Master_CLSS_Executive_Dashboard.html',
    'RSK_Master_CLSS_Executive_Studio_Enhanced.html'
]

def patch_file(filepath):
    print(f"[*] Processing {filepath}...", flush=True)
    if not os.path.exists(filepath):
        print(f"[-] File not found: {filepath}")
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern for old refreshQuestionBankDropdown filter check
    old_filter_pattern = r'(function refreshQuestionBankDropdown\(\)\s*\{[\s\S]*?const filtered = surveys\.filter\(s => \{[\s\S]*?)(if \(roleFilter !== \'ALL\' && s\.cadre\) \{[\s\S]*?return true;\s*\}\);)'
    
    new_filter_replacement = r'''\1if (roleFilter !== 'ALL') {
          const rawRole = (s.role || s.cadre || '').toLowerCase();
          const rLower = roleFilter.toLowerCase();
          if (rLower.includes('part') || rLower.includes('teach')) {
            if (!rawRole.includes('part') && !rawRole.includes('teach')) return false;
          } else if (rLower.includes('fac')) {
            if (!rawRole.includes('fac')) return false;
          } else if (rLower.includes('obs') || rLower.includes('mon')) {
            if (!rawRole.includes('mon') && !rawRole.includes('obs')) return false;
          }
        }
        return true;
      });'''

    if 'const rawRole = (s.role || s.cadre' not in content:
        new_content, count = re.subn(old_filter_pattern, new_filter_replacement, content, count=1)
        if count > 0:
            content = new_content
            print("  [+] Successfully patched refreshQuestionBankDropdown() role filtering")
        else:
            print("  [-] Regex match failed for refreshQuestionBankDropdown()")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"[✓] Successfully updated {filepath}\n")
    return True

def main():
    print("===================================================================")
    print(" Applying Tab 6 Question Bank Role Slicer Fix Across All Targets")
    print("===================================================================\n")
    for target in TARGET_FILES:
        patch_file(target)

if __name__ == '__main__':
    main()
