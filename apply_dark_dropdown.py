import glob
import re

files = glob.glob('*.html')

new_mobile_nav_css = """      nav .nav-links,
      nav .search-wrap,
      nav .top-right-lang {
        display: none !important;
      }

      .hamburger {
        display: flex !important;
      }

      nav.open .nav-links {
        display: flex !important;
        flex-direction: column;
        position: absolute;
        top: 60px;
        right: 0;
        left: auto;
        width: 260px;
        background: #111 !important;
        padding: 1.5rem 0;
        gap: 0;
        z-index: 999;
        box-shadow: -5px 10px 20px rgba(0, 0, 0, 0.5);
        border: none;
      }

      nav.open .nav-links li {
        width: 100%;
        margin: 0;
      }

      nav.open .nav-links a {
        color: #ddd !important;
        padding: 1rem 2rem !important;
        display: block !important;
        width: 100%;
        text-align: left !important;
        font-weight: 500;
        font-size: 1rem;
        transition: 0.3s ease;
        border: none !important;
        background: transparent !important;
      }

      nav.open .nav-links a:hover {
        background: #222 !important;
        color: #fff !important;
      }

      nav.open .nav-links .nav-cta {
        margin: 1rem 2rem 0 2rem !important;
        width: calc(100% - 4rem) !important;
        text-align: center !important;
        background: #DB1A1A !important;
        color: #FFF !important;
        padding: 0.8rem !important;
        border-radius: 4px;
      }"""

# regex to find the old nav.open CSS inside @media (max-width: 900px)
# We will replace from "nav .nav-links," up to the end of "nav.open .nav-links { ... }" block

for f in files:
    if "google" in f: continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

    # 1. Remove Çözüm 2 block
    content = re.sub(r"/\* Masaüstünü etkilemeyecek, sadece 1200px altındaki ekranlarda çalışacak kodlar \(Çözüm 2\)\ \*/.*?\}\s*\}", "", content, flags=re.DOTALL)
    
    # 2. Replace the inner CSS inside @media 900px
    # We look for "nav .nav-links," and replace it and everything up to the end of the box-shadow: ... } block
    pattern = r"nav \.nav-links,\s*nav \.search-wrap\s*\{\s*display:\s*none;\s*\}\s*\.hamburger\s*\{\s*display:\s*flex;\s*\}\s*nav\.open \.nav-links\s*\{.*?\}"
    
    content = re.sub(pattern, new_mobile_nav_css, content, flags=re.DOTALL)

    # 3. Make sure toggleMenu is not broken
    # Ensure there is a toggleMenu function in the HTML if it doesn't exist
    if "function toggleMenu()" not in content:
        toggle_script = """<script>
    function toggleMenu() {
      const nav = document.getElementById('navbar');
      nav.classList.toggle('open');
    }
  </script>
</body>"""
        content = content.replace("</body>", toggle_script)

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
        
    print(f"Applied dark dropdown to {f}")
