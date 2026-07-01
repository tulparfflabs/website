import glob
import re

files = glob.glob('*.html')

old_logic_pattern = r"function forceMobileNav\(\)\s*\{[\s\S]*?\}\s*window\.addEventListener"

new_forceMobileNav = """function forceMobileNav() {
      var navLinks = document.querySelector('.nav-links');
      var hamburger = document.querySelector('.hamburger');
      var nav = document.getElementById('navbar');
      var searchWrap = document.querySelector('.search-wrap');
      var topLang = document.querySelector('.top-right-lang');

      var isMobile = window.innerWidth <= 1200 || navigator.userAgent.match(/Mobi|Android|iPhone|iPad/i);

      if (isMobile) {
        if (hamburger) {
          hamburger.style.setProperty('display', 'flex', 'important');
        }
        if (searchWrap) {
          searchWrap.style.setProperty('display', 'none', 'important');
        }
        if (topLang) {
          topLang.style.setProperty('display', 'none', 'important');
        }
        if (navLinks) {
          if (!nav || !nav.classList.contains('open')) {
            navLinks.style.setProperty('display', 'none', 'important');
          } else {
            navLinks.style.setProperty('display', 'flex', 'important');
            navLinks.style.setProperty('flex-direction', 'column', 'important');
            navLinks.style.setProperty('position', 'absolute', 'important');
            navLinks.style.setProperty('top', '70px', 'important');
            navLinks.style.setProperty('left', '0', 'important');
            navLinks.style.setProperty('right', '0', 'important');
            navLinks.style.setProperty('background', 'rgba(255, 255, 255, 0.98)', 'important');
            navLinks.style.setProperty('padding', '20px 0', 'important');
            navLinks.style.setProperty('box-shadow', '0 10px 30px rgba(0, 0, 0, 0.1)', 'important');

            var cta = navLinks.querySelector('.nav-cta');
            if (cta) {
              cta.style.setProperty('display', 'block', 'important');
              cta.style.setProperty('background', '#DB1A1A', 'important');
              cta.style.setProperty('color', '#FFF', 'important');
              cta.style.setProperty('margin-top', '15px', 'important');
              cta.style.setProperty('width', '100%', 'important');
              cta.style.setProperty('text-align', 'center', 'important');
            }
            
            var listItems = navLinks.querySelectorAll('li');
            listItems.forEach(li => {
               li.style.setProperty('width', '100%', 'important');
               li.style.setProperty('text-align', 'center', 'important');
            });
            var linkItems = navLinks.querySelectorAll('a:not(.nav-cta)');
            linkItems.forEach(a => {
               a.style.setProperty('display', 'block', 'important');
               a.style.setProperty('padding', '10px 0', 'important');
            });
          }
        }
      } else {
        if (navLinks) {
          navLinks.style.removeProperty('display');
          navLinks.style.removeProperty('flex-direction');
          navLinks.style.removeProperty('position');
          navLinks.style.removeProperty('top');
          navLinks.style.removeProperty('left');
          navLinks.style.removeProperty('right');
          navLinks.style.removeProperty('background');
          navLinks.style.removeProperty('padding');
          navLinks.style.removeProperty('box-shadow');
          
          var cta = navLinks.querySelector('.nav-cta');
          if (cta) {
             cta.style.removeProperty('display');
             cta.style.removeProperty('background');
             cta.style.removeProperty('color');
             cta.style.removeProperty('margin-top');
             cta.style.removeProperty('width');
             cta.style.removeProperty('text-align');
          }
          var listItems = navLinks.querySelectorAll('li');
          listItems.forEach(li => {
             li.style.removeProperty('width');
             li.style.removeProperty('text-align');
          });
          var linkItems = navLinks.querySelectorAll('a:not(.nav-cta)');
          linkItems.forEach(a => {
             a.style.removeProperty('display');
             a.style.removeProperty('padding');
          });
        }
        if (hamburger) hamburger.style.removeProperty('display');
        if (searchWrap) searchWrap.style.removeProperty('display');
        if (topLang) topLang.style.removeProperty('display');
      }
    }
    window.addEventListener"""

for f in files:
    if "google" in f: continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    content = re.sub(old_logic_pattern, new_forceMobileNav, content)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Updated {f}")
