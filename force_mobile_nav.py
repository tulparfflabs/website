import glob

html_files = glob.glob('*.html')

js_snippet = """
  <script>
    // --- Force Mobile Nav Fix ---
    function forceMobileNav() {
      if(window.innerWidth <= 1024) {
        var navLinks = document.querySelector('.nav-links');
        var hamburger = document.querySelector('.hamburger');
        var nav = document.getElementById('navbar');
        var searchWrap = document.querySelector('.search-wrap');
        var topLang = document.querySelector('.top-right-lang');
        
        if(navLinks && (!nav || !nav.classList.contains('open'))) {
          navLinks.style.setProperty('display', 'none', 'important');
        }
        if(hamburger) {
          hamburger.style.setProperty('display', 'flex', 'important');
        }
        if(searchWrap) {
          searchWrap.style.setProperty('display', 'none', 'important');
        }
        if(topLang) {
          topLang.style.setProperty('display', 'none', 'important');
        }
      } else {
        var navLinks = document.querySelector('.nav-links');
        var hamburger = document.querySelector('.hamburger');
        var searchWrap = document.querySelector('.search-wrap');
        var topLang = document.querySelector('.top-right-lang');
        
        if(navLinks) navLinks.style.removeProperty('display');
        if(hamburger) hamburger.style.removeProperty('display');
        if(searchWrap) searchWrap.style.removeProperty('display');
        if(topLang) topLang.style.removeProperty('display');
      }
    }
    window.addEventListener('resize', forceMobileNav);
    window.addEventListener('load', forceMobileNav);
    document.addEventListener('DOMContentLoaded', forceMobileNav);
    forceMobileNav();
  </script>
</body>
"""

for file_path in html_files:
    if "google" in file_path: continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "Force Mobile Nav Fix" not in content:
        if "</body>" in content:
            new_content = content.replace("</body>", js_snippet)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Applied JS fix to {file_path}")
