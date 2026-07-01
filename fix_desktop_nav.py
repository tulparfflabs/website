import glob
import re

files = glob.glob('*.html')

for f in files:
    if "google" in f: continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

    # The block that ruined the desktop layout by expanding the nav container
    bad_nav_block = """    nav {
       height: auto !important;
       overflow: visible !important;
    }"""
    
    # Another variation without indentation just in case
    bad_nav_block2 = """nav {
       height: auto !important;
       overflow: visible !important;
    }"""
    
    # Aggressive regex replacement for the bad block
    content = re.sub(r'nav\s*\{\s*height:\s*auto\s*!important;\s*overflow:\s*visible\s*!important;\s*\}', '', content, flags=re.DOTALL)

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
        
    print(f"Fixed desktop nav layout in {f}")
