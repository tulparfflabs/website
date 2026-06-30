import glob

html_files = glob.glob('*.html')

fixed_css = """
    /* --- Responsive Conversion Guide Additions --- */
    img, canvas {
      max-width: 100%;
      height: auto;
    }
    
    /* Yalnızca ana butonlarda dokunma alanı */
    @media (max-width: 768px) {
      .btn-primary, .btn-secondary, .nav-links a {
        min-height: 48px;
        display: flex;
        align-items: center;
        justify-content: center;
      }
    }
"""

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We need to replace the old block with the fixed one.
    import re
    # The old block was between /* --- Responsive Conversion Guide Additions --- */ and </style>
    # Let's find the old block and replace it.
    old_block_start = "/* --- Responsive Conversion Guide Additions --- */"
    if old_block_start in content:
        start_idx = content.find(old_block_start)
        end_idx = content.find("</style>", start_idx)
        if end_idx != -1:
            new_content = content[:start_idx] + fixed_css + "\n  " + content[end_idx:]
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed {file_path}")
    else:
        print(f"Skipping {file_path}, block not found.")
