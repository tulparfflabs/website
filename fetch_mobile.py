import urllib.request
try:
    req = urllib.request.Request('https://tulparff.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1'})
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    with open('live_test_mobile.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('Fetched live_test_mobile.html')
except Exception as e:
    print(f'Error: {e}')
