import urllib.request
try:
    req = urllib.request.Request('https://tulparff.com/', headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    if 'FALLBACK MOBILE OVERRIDE' in html:
        print('YES FALLBACK')
    else:
        print('NO FALLBACK')
except Exception as e:
    print(f'Error: {e}')
