import urllib.request
try:
    req = urllib.request.Request('https://tulparff.com', headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read().decode('utf-8')
    if 'id="hamburger"' in html:
        print('LIVE SITE HAS MY FIX (hamburger id found)')
    else:
        print('LIVE SITE DOES NOT HAVE MY FIX (hamburger id missing)')
        
    if 'display: flex !important;' in html:
        print('LIVE SITE HAS SOME OF MY CSS')
    else:
        print('LIVE SITE DOES NOT HAVE CSS')
except Exception as e:
    print('Failed to fetch:', e)
