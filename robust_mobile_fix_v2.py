import glob

html_files = glob.glob('*.html')

robust_css = """
    /* --- Robust Mobile Navigation Fix v2 --- */
    @media screen and (max-width: 1024px) {
      nav .nav-links {
        display: none !important;
      }
      nav.open .nav-links {
        display: flex !important;
        flex-direction: column !important;
        position: absolute !important;
        top: 60px !important;
        left: 0 !important;
        right: 0 !important;
        background: rgba(255, 255, 255, 0.98) !important;
        padding: 20px 0 !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1) !important;
      }
      nav.open .nav-links li {
        width: 100% !important;
        text-align: center !important;
      }
      nav.open .nav-links a {
        display: block !important;
        padding: 10px 0 !important;
        color: var(--text) !important;
      }
      .hamburger {
        display: flex !important;
      }
      /* Hide the redundant floating lang button on mobile since we have one in nav */
      .top-right-lang {
        display: none !important;
      }
      nav .search-wrap {
        display: none !important;
      }
    }
"""

for file_path in html_files:
    if "google" in file_path: continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "/* --- Robust Mobile Navigation Fix v2 --- */" not in content:
        # We need to replace the old v1 block if it exists
        if "/* --- Robust Mobile Navigation Fix --- */" in content:
            import re
            content = re.sub(r'/\* --- Robust Mobile Navigation Fix --- \*/.*?(?=</style>)', robust_css + '\n  ', content, flags=re.DOTALL)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated robust mobile CSS to v2 in {file_path}")
