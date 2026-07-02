import os
import re
import shutil

html_files = ['index.html', 'team.html', 'contact.html', 'vehicle.html', 'blog.html', 'blog-yolo11.html']

# 1. Backups
print("Creating backups...")
for f in html_files:
    if os.path.exists(f):
        shutil.copy(f, f + '.bak')
        print(f"Backed up {f}")

# 2. Extract CSS from index.html
print("\nExtracting CSS from index.html...")
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'<style>(.*?)</style>', content, re.DOTALL | re.IGNORECASE)
if match:
    css_content = match.group(1).strip()
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css_content)
    print("Extracted CSS to style.css")
else:
    print("ERROR: Could not find <style> block in index.html")
    exit(1)

# 3. Process all files
print("\nProcessing HTML files...")
link_tag = '<link rel="stylesheet" href="style.css">'
for f in html_files:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        if link_tag not in content:
            # Check if there is any <style> block
            if re.search(r'<style>.*?</style>', content, re.DOTALL | re.IGNORECASE):
                # Replace the first one with the link
                content = re.sub(r'<style>.*?</style>', link_tag, content, count=1, flags=re.DOTALL | re.IGNORECASE)
                # Remove any subsequent <style> blocks (like the second one in vehicle.html)
                content = re.sub(r'<style>.*?</style>', '', content, flags=re.DOTALL | re.IGNORECASE)
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Processed {f}")

# 4. Fix SVG typo in index.html
print("\nFixing SVG typo in index.html...")
with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# We look for the exact string or use regex
old_svg = '<svg class="splash-drone" width="130" height="96" viewBox="0 0 130 96" fill="none">\n      xmlns="http://www.w3.org/2000/svg">'
old_svg2 = '<svg class="splash-drone" width="130" height="96" viewBox="0 0 130 96" fill="none">\nxmlns="http://www.w3.org/2000/svg">'
new_svg = '<svg class="splash-drone" width="130" height="96" viewBox="0 0 130 96" fill="none" xmlns="http://www.w3.org/2000/svg">'

if old_svg in idx_content:
    idx_content = idx_content.replace(old_svg, new_svg)
    print("Fixed SVG typo (format 1)")
elif old_svg2 in idx_content:
    idx_content = idx_content.replace(old_svg2, new_svg)
    print("Fixed SVG typo (format 2)")
else:
    # Try regex
    match = re.search(r'<svg class="splash-drone" width="130" height="96" viewBox="0 0 130 96" fill="none">\s*xmlns="http://www.w3.org/2000/svg">', idx_content)
    if match:
        idx_content = idx_content.replace(match.group(0), new_svg)
        print("Fixed SVG typo (regex)")
    else:
        print("SVG typo not found or already fixed.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx_content)

print("\nDone!")
