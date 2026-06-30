import glob

html_files = glob.glob('*.html')

robust_css = """
    /* --- Robust Mobile Navigation Fix --- */
    @media screen and (max-width: 1024px) {
      nav .nav-links {
        display: none !important;
      }
      nav.open .nav-links {
        display: flex !important;
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
    # skip the google verification file
    if "google" in file_path: continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "/* --- Robust Mobile Navigation Fix --- */" not in content:
        if "</style>" in content:
            new_content = content.replace("</style>", robust_css + "\n  </style>")
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Applied robust mobile CSS to {file_path}")
