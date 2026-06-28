import re
import sys

def get_file_content(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file_content(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

index_content = get_file_content('index.html')

style_match = re.search(r'<style>(.*?)</style>', index_content, re.DOTALL)
index_style = style_match.group(1) if style_match else ''

# Split index_style at @media (max-width: 900px) {
split_marker = '@media (max-width: 900px) {'
parts = index_style.split(split_marker)
if len(parts) == 2:
    index_style_top = parts[0]
    index_style_bottom = split_marker + parts[1]
else:
    print("Could not find media queries marker in index.html")
    sys.exit(1)

files = ['contact.html', 'team.html', 'vehicle.html']

for file in files:
    content = get_file_content(file)
    target_style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
    if not target_style_match: continue
    target_style = target_style_match.group(1)
    
    # Extract specific CSS from the current file
    # We look between "@keyframes fill { to { width: 100%; } }" and "a:focus-visible"
    specific_match = re.search(r'@keyframes fill\s*\{\s*to\s*\{\s*width:\s*100%;\s*\}\s*\}(.*?)(?:a:focus-visible|@media)', target_style, re.DOTALL)
    if specific_match:
        specific_css = specific_match.group(1).strip()
        
        # Clean up any accidental media query rules that were inserted without the wrapper
        # in the previous script (like .about-grid, .contact-grid { grid-template-columns: 1fr; })
        nav_links_a = "  .nav-links a { font-size: 0.875rem; color: #FFF; text-decoration: none; letter-spacing: 0.05em; text-transform: uppercase; padding: 6px 14px; border: 2px solid var(--accent2); background: transparent; border-radius: 6px; font-weight: 700; transition: all 0.3s ease; }\n  .nav-links a:hover { background: var(--accent2); color: #FFF; }"
        specific_css_lines = specific_css.split('\n')
        clean_lines = []
        for line in specific_css_lines:
            if 'grid-template-columns: 1fr;' in line and 'contact-grid' in line:
                continue # Skip this accidental rule
            if 'grid-template-columns: 1fr 1fr;' in line and 'blog-grid' in line:
                continue
            if 'grid-template-columns: repeat(2,1fr);' in line:
                continue
            clean_lines.append(line)
        specific_css = '\n'.join(clean_lines).strip()
        
        new_style = index_style_top + "\n  /* --- PAGE SPECIFIC STYLES --- */\n  " + specific_css + "\n\n  " + index_style_bottom
        
        content = content[:target_style_match.start(1)] + "\n" + new_style + "\n" + content[target_style_match.end(1):]
        write_file_content(file, content)
        print(f"Fixed styles in {file}")
    else:
        print(f"Could not extract specific CSS from {file}")

