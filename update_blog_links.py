import glob
import re

for filename in glob.glob('*.html'):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace href="#blog" or href="index.html#blog" with href="blog.html"
    new_content = re.sub(r'href=[\"\'\'](?:index\.html)?#blog[\"\'\']', 'href=\"blog.html\"', content)
    
    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
