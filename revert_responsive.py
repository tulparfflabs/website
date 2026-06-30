import glob

html_files = glob.glob('*.html')

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    start_marker = "/* --- Responsive Conversion Guide Additions --- */"
    if start_marker in content:
        start_idx = content.find(start_marker)
        end_idx = content.find("</style>", start_idx)
        if end_idx != -1:
            # Remove the block entirely
            new_content = content[:start_idx] + "\n  " + content[end_idx:]
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Reverted {file_path}")
    else:
        print(f"Skipping {file_path}, block not found.")
