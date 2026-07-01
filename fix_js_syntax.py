import glob
import re

files = glob.glob('*.html')

for f in files:
    if "google" in f: continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

    # The dangling block left behind by the bad regex:
    dangling_block = """      if (btn) {
        btn.setAttribute('aria-expanded', isOpen);
      }
      if (typeof forceMobileNav === 'function') {
        forceMobileNav();
      }
    }"""
    
    # We also have an event listener that references the old hamburger id and the old toggle logic:
    dangling_event_listener = """    document.querySelectorAll('.nav-links a').forEach(a => {
      a.addEventListener('click', () => {
        document.getElementById('navbar').classList.remove('open');
        document.getElementById('hamburger').setAttribute('aria-expanded', 'false');
      });
    });"""

    if dangling_block in content:
        content = content.replace(dangling_block, '')
        
    if dangling_event_listener in content:
        content = content.replace(dangling_event_listener, '')
        
    # There is also one more variation of the dangling block if the regex matched slightly differently:
    # Let's just use a regex to aggressively remove anything looking like it
    content = re.sub(r'\s*if\s*\(\s*btn\s*\)\s*\{\s*btn\.setAttribute\(\'aria-expanded\',.*?\s*\}\s*', '', content, flags=re.DOTALL)
    content = re.sub(r'\s*if\s*\(\s*typeof forceMobileNav === \'function\'\s*\)\s*\{\s*forceMobileNav\(\);\s*\}\s*\}\s*', '', content, flags=re.DOTALL)

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
        
    print(f"Fixed JS syntax in {f}")
