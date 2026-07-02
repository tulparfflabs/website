import re

with open('live_test_mobile.html', 'r', encoding='utf-8') as f:
    html = f.read()

head = re.search(r'<head>(.*?)</head>', html, re.DOTALL)
if head:
    print(head.group(1).strip()[:1000])
