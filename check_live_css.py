import re

with open('live_test_mobile.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract the style tag
style_match = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
if not style_match:
    print('No style tag found')
    exit()

css = style_match.group(1)

# Find all @media rules
media_queries = re.findall(r'@media[^{]+\{', css)
print('Media queries found in live site:')
for mq in media_queries:
    print(mq)

