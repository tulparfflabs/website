import re

with open('live_test_mobile.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract script tags
script_matches = re.findall(r'<script.*?>(.*?)</script>', html, re.DOTALL)
for i, js in enumerate(script_matches):
    if 'nav-links' in js or 'display' in js:
        print(f'Script {i} contains potential overrides:')
        lines = js.split('\n')
        for i, line in enumerate(lines):
            if 'nav-link' in line or 'style' in line or 'display' in line:
                print(f"{i}: {line.strip()}")
