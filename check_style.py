import os
html_files = ['index.html', 'team.html', 'contact.html', 'vehicle.html', 'blog.html', 'blog-yolo11.html']
for f in html_files:
    if os.path.exists(f):
        content = open(f, 'r', encoding='utf-8').read()
        print(f"{f}: {content.count('<style>')} <style>, {content.count('</style>')} </style>")
