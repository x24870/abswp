# Verify if the link on the web is accessable
# Usage: python linkVerfication.py URL

import requests, sys, bs4

def linkVerificarion(url):
    resp = requests.get(url)
    
    soup = bs4.BeautifulSoup(resp.text, 'html5lib')
    
    for link in soup.select('a[href]'):
        linkUrl = link['href']
        try:
            print('Try to accessing {} ...'.format(linkUrl))
            requests.get(linkUrl)
        except Exception:
            print('NOT accessable: {}'.format(linkUrl))
        
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python linkVerfication.py URL')
    else:
        url = sys.argv[1]
        if not url.startswith('https://'):
            url = 'https://' + url
        print('Verify link: {}'.format(url))
        linkVerificarion(url)


