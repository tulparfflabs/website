import glob
import re

files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Add inline onclick to hamburger
    # We replace any existing <div class="hamburger-menu" id="hamburger"...> with the inline onclick version.
    # Be careful not to duplicate it if it already has onclick.
    content = re.sub(
        r'<div class="hamburger-menu" id="hamburger"(?: onclick=".*?")?>',
        '<div class="hamburger-menu" id="hamburger" onclick="document.querySelector(\'.nav-links\').classList.toggle(\'aktif\')">',
        content
    )
    
    # 2. Add margin-right to .nav-right in mobile media query
    if '@media screen and (max-width: 1200px) {' in content:
        # Check if we already added it
        if '.nav-right {' not in content.split('@media screen and (max-width: 1200px) {')[1][:500]:
            content = content.replace(
                '@media screen and (max-width: 1200px) {',
                '@media screen and (max-width: 1200px) {\n        .nav-right {\n            margin-right: 60px !important;\n        }'
            )
            
    # 3. Add background and padding to hamburger to ensure it stands out
    # Only if it doesn't already have background: #f0f0f0
    if 'background: #f0f0f0;' not in content:
        content = re.sub(
            r'\.hamburger-menu\s*\{\s*display:\s*none;',
            '.hamburger-menu {\n        display: none;\n        background: #f0f0f0;\n        padding: 8px;\n        border-radius: 5px;\n        border: 1px solid #ccc;',
            content
        )
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
        
    print(f'Updated {f}')
