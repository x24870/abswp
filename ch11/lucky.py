import requests, webbrowser, sys, bs4

def googleSearch(keyword):
    print('KEYWORD: ' , keyword)
    url = 'https://www.google.com.tw/search?q=' + keyword
    resp = requests.get(url)
    resp.raise_for_status()
    
    soup = bs4.BeautifulSoup(resp.text, 'html5lib')
    
    link = soup.select('.r a')
    
    numOpen = min(5, len(link))
    
    for i in range(numOpen):
        webbrowser.open('http://google.com' + link[i].get('href'))
        print(link[i].get('href'))
    

if len(sys.argv) < 2:
    print('Usage: $python lucky.py KEYWORD_TO_SEARCH')
else:
    googleSearch(' '.join(sys.argv[1:]))