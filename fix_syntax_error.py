import glob
import re

html_files = glob.glob('*.html')

clean_toggle_menu = """function toggleMenu() {
      const nav = document.getElementById('navbar');
      const btn = document.querySelector('.hamburger');
      let isOpen = false;
      if(nav) {
        isOpen = nav.classList.toggle('open');
      }
      if(btn) {
        btn.setAttribute('aria-expanded', isOpen);
      }
      if(typeof forceMobileNav === 'function') {
        forceMobileNav();
      }
    }"""

for file_path in html_files:
    if "google" in file_path: continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regex to find the corrupted toggleMenu and replace it
    # The corrupted one starts with function toggleMenu() { and ends with }
    # We need to be careful with re.DOTALL to only match the first } after toggleMenu()
    
    new_content = re.sub(
        r'function toggleMenu\(\)\s*\{[^{}]*\}',
        clean_toggle_menu,
        content
    )
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed JS syntax error in {file_path}")
    else:
        print(f"No changes made to {file_path}")
