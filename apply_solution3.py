import glob
import re

files = glob.glob('*.html')

css_to_replace = """
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

css_new = """
    /* Masaüstünü etkilemeyecek, sadece 1200px altındaki ekranlarda çalışacak kodlar (Çözüm 2) */
    @media screen and (max-width: 1200px) {
        nav, #navbar {
            height: auto !important;
            overflow: visible !important;
            padding-bottom: 10px !important;
            padding-top: 10px !important;
        }
        .nav-links {
            display: flex !important;
            flex-wrap: wrap !important;
            justify-content: center !important;
            row-gap: 10px !important;
            gap: 10px !important;
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
    
    # Replace the old Çözüm 2 with the new one
    if css_to_replace.strip() in content:
        content = content.replace(css_to_replace.strip(), css_new.strip())
    elif "Çözüm 2" in content:
        # Fallback if whitespace differs
        content = re.sub(r"/\* Masaüstünü etkilemeyecek, sadece 1200px altındaki ekranlarda çalışacak kodlar \(Çözüm 2\)\ \*/.*?\}\s*\}", css_new.strip(), content, flags=re.DOTALL)
    else:
        # If not there, inject it before </style>
        content = content.replace("</style>", css_new + "\n  </style>")
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
        
    print(f"Applied Updated Solution 2 to {f}")
