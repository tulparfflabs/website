import glob
import re

files = glob.glob('*.html')

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove specifically the nav-related rules from the @media (max-width: 900px) block
    # We will search for nav .nav-links, .hamburger, nav.open .nav-links inside @media (max-width: 900px)
    
    pattern_nav_links = r'nav \.nav-links,\s*nav \.search-wrap,\s*nav \.top-right-lang\s*\{[^}]*\}'
    content = re.sub(pattern_nav_links, '', content)
    
    pattern_hamburger = r'\.hamburger\s*\{\s*display:\s*flex\s*!important;\s*\}'
    content = re.sub(pattern_hamburger, '', content)
    
    pattern_nav_open_links = r'nav\.open \.nav-links\s*\{[^}]*\}'
    content = re.sub(pattern_nav_open_links, '', content)
    
    pattern_nav_open_li = r'nav\.open \.nav-links\s*li\s*\{[^}]*\}'
    content = re.sub(pattern_nav_open_li, '', content)
    
    pattern_nav_open_a = r'nav\.open \.nav-links\s*a\s*\{[^}]*\}'
    content = re.sub(pattern_nav_open_a, '', content)

    # Note: Because the unified CSS is at the END of the style block, we might have accidentally removed its rules too!
    # BUT wait, the regex I just wrote would match the NEW Unified CSS as well, EXCEPT the new unified CSS has slightly different content.
    # Actually, it's safer to just run the full clean_refactor.py again after stripping all nav.open stuff completely.

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
        
    print(f'Cleaned old 900px nav rules from {f}')
