import re

def main():
    files = ['RSK_Master_CLSS_Executive_Studio_Enhanced.html', 'RSK_Master_CLSS_Executive_Dashboard.html', 'index.html', 'deploy/index.html']
    
    for fpath in files:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the donut chart colors
        # Old: backgroundColor: ['#1d4ed8', '#008aab', '#4f46e5']
        # New: backgroundColor: ['#008aab', '#10b981', '#f59e0b']
        old_pattern = r"backgroundColor:\s*\[\s*['\"]#1d4ed8['\"]\s*,\s*['\"]#008aab['\"]\s*,\s*['\"]#4f46e5['\"]\s*\]"
        new_colors = "backgroundColor: ['#008aab', '#10b981', '#f59e0b']"
        
        updated_content = re.sub(old_pattern, new_colors, content)
        
        if updated_content != content:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f'Updated donut colors in {fpath} successfully!')
        else:
            print(f'Pattern not matched directly in {fpath}, checking manual replace')
            if "['#1d4ed8', '#008aab', '#4f46e5']" in content:
                content = content.replace("['#1d4ed8', '#008aab', '#4f46e5']", "['#008aab', '#10b981', '#f59e0b']")
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f'Replaced literal in {fpath} successfully!')

if __name__ == '__main__':
    main()
