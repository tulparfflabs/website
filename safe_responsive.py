import glob

html_files = glob.glob('*.html')

safe_css = """
    /* --- Responsive Conversion Guide Additions --- */
    img {
      max-width: 100%;
      height: auto;
    }
"""

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "/* --- Responsive Conversion Guide Additions --- */" not in content:
        if "</style>" in content:
            new_content = content.replace("</style>", safe_css + "\n  </style>")
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Applied safe CSS to {file_path}")
