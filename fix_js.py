import glob
import re

files = glob.glob('*.html')

old_logic = r"if\s*\(\s*navLinks\s*&&\s*\(!nav\s*\|\|\s*!nav\.classList\.contains\('open'\)\)\)\s*\{\s*navLinks\.style\.setProperty\('display',\s*'none',\s*'important'\);\s*\}"

new_logic = """if (navLinks) {
          if (!nav || !nav.classList.contains('open')) {
            navLinks.style.setProperty('display', 'none', 'important');
          } else {
            navLinks.style.removeProperty('display');
          }
        }"""

for f in files:
    if "google" in f: continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    content = re.sub(old_logic, new_logic, content)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Updated {f}")
