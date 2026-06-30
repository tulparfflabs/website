import glob

css_to_add = """
    /* --- Responsive Conversion Guide Additions --- */
    img, video, canvas {
      max-width: 100%;
      height: auto;
    }
    
    @media (max-width: 768px) {
      /* Dokunma Alanları (Tappable Areas) - min 48px */
      a, button, .btn-primary, .btn-secondary {
        min-height: 48px;
      }
      
      .nav-links a {
        display: flex;
        align-items: center;
      }
    }
"""

html_files = glob.glob('*.html')

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "/* --- Responsive Conversion Guide Additions --- */" in content:
        print(f"Skipping {file_path}, already added.")
        continue

    # Insert right before </style>
    if "</style>" in content:
        new_content = content.replace("</style>", css_to_add + "\n  </style>")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file_path}")
    else:
        print(f"No <style> tag found in {file_path}")
