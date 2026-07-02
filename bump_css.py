import os
import re

folders = [
    r"C:\Users\bahsi\OneDrive\Belgeler\GitHub\website",
    r"C:\Users\bahsi\OneDrive\Masaüstü\tulpar-ff - Kopya"
]

for folder in folders:
    for filename in os.listdir(folder):
        if filename.endswith('.html'):
            filepath = os.path.join(folder, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Change breakpoint from 992px to 1200px
            content = content.replace('@media screen and (max-width: 992px)', '@media screen and (max-width: 1200px)')
            
            # Change background-color of hamburger spans to be explicitly visible
            content = content.replace('background-color: var(--text);', 'background-color: #0F172A !important;')

            # Boost z-index to be absolutely sure
            content = content.replace('z-index: 1001;', 'z-index: 20000 !important;')
            content = content.replace('z-index: 1000;', 'z-index: 19999 !important;')

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

print("Updated HTML files in both folders.")
