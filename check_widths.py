import re

with open('live_test_mobile.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find any inline styles with width > 1200px or min-width > 1200px
widths = re.findall(r'width:\s*(\d+)px', html)
min_widths = re.findall(r'min-width:\s*(\d+)px', html)

print('widths:', [w for w in widths if int(w) > 400])
print('min_widths:', [w for w in min_widths if int(w) > 400])
