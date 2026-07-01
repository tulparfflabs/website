import glob

files = glob.glob('*.html')

for f in files:
    if "google" in f: continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

    # Change hamburger color from white to dark gray so it's visible on the white navbar
    if "background-color: #fff; /* Sitenin" in content or "background-color: #fff;" in content:
        # specifically replace the hamburger span color
        import re
        content = re.sub(r'(\.hamburger-menu\s*span\s*\{[^}]*?background-color:\s*)#fff(;| !important;)', r'\1#333\2', content)

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
        
    print(f"Fixed hamburger color in {f}")
