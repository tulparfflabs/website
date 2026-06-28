# -*- coding: utf-8 -*-
import glob
import re

for filepath in glob.glob('*.html'):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = re.sub(r'\s*<li><a href=\"[^\"]*blog[^\"]*\".*?>Blog</a></li>', '', content, flags=re.IGNORECASE)
        
        def replacer(match):
            return match.group(0) + '\n      <li><a href="blog.html" data-tr="Blog" data-en="Blog">Blog</a></li>'
            
        content = re.sub(r'(<li><a href=\"vehicle\.html\"[^>]*>Ara\u00e7</a></li>)', replacer, content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated " + filepath)
    except Exception as e:
        print("Error updating " + filepath + ": " + str(e))

