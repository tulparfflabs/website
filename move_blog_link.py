# -*- coding: utf-8 -*-
import glob
import re

for filepath in glob.glob('*.html'):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. Remove existing Blog link
        content = re.sub(r'\s*<li><a href=\"blog\.html\" data-tr=\"Blog\" data-en=\"Blog\">Blog</a></li>', '', content)
        
        # 2. Add Blog link right after Takım link
        # It could be Takım, Takm, etc. So I'll match the team.html part.
        def replacer(match):
            return match.group(0) + '\n      <li><a href="blog.html" data-tr="Blog" data-en="Blog">Blog</a></li>'
            
        content = re.sub(r'(<li><a href=\"team\.html\"[^>]*>.*?</a></li>)', replacer, content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated " + filepath)
    except Exception as e:
        print("Error updating " + filepath + ": " + str(e))
