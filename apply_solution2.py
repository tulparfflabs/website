import glob
import re
import os

files = glob.glob('*.html')

# The regex to find and remove the forceMobileNav script block
script_pattern = r"(?s)// --- Force Mobile Nav Fix ---.*?(?=</script>)"

# The CSS to inject before </style>
css_to_inject = """
    /* Masaüstünü etkilemeyecek, sadece 1200px altındaki ekranlarda çalışacak kodlar (Çözüm 2) */
    @media screen and (max-width: 1200px) {
        .nav-links {
            display: flex !important;
            flex-wrap: wrap !important;
            justify-content: center !important;
            row-gap: 10px;
        }
        .hamburger {
            display: none !important;
        }
    }
"""

for f in files:
    if "google" in f: continue
    
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Remove the forceMobileNav JS
    content = re.sub(script_pattern, "", content)
    
    # 2. Add the CSS before </style>
    if "Çözüm 2" not in content:
        content = content.replace("</style>", css_to_inject + "\n  </style>")
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
        
    print(f"Applied Solution 2 to {f}")
