import urllib.request
import re

try:
    req = urllib.request.Request('https://tulparff.com/?v=123', headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read().decode('utf-8')
    res = re.findall(r'<link[^>]*rel="stylesheet"[^>]*>', html, re.IGNORECASE)
    print('External stylesheets:', res)
    
    # Also find if there are multiple style blocks
    style_blocks = re.findall(r'<style', html, re.IGNORECASE)
    print(f'Number of style blocks: {len(style_blocks)}')
except Exception as e:
    print('Failed:', e)
