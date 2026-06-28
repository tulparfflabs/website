import os

files_to_fix = ["vehicle.html", "blog.html", "blog-yolo11.html", "contact.html"]

bad_lines = [
    ".nav-links a { font-size: 0.875rem; color: #FFF !important; text-decoration: none; letter-spacing: 0.05em; text-transform: uppercase; padding: 6px 14px; border: 2px solid #DB1A1A !important; background: #DB1A1A !important; border-radius: 6px; font-weight: 700; transition: all 0.3s ease; display: inline-block; }",
    ".nav-links a:hover { background: transparent !important; color: #DB1A1A !important; }",
    ".nav-cta { box-shadow: 0 4px 15px rgba(219, 26, 26, 0.3); }"
]

for file in files_to_fix:
    if not os.path.exists(file):
        continue
    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    new_lines = []
    for line in lines:
        skip = False
        for bad in bad_lines:
            if bad in line:
                skip = True
                break
        if not skip:
            new_lines.append(line)
            
    with open(file, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    print(f"Fixed {file}")
