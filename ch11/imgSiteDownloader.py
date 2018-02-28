# Download images from https://www.deviantart.com/
# Usage: python imgSiteDownloader.py KEYWORD

url = 'https://www.deviantart.com/'
searchUrl = 'https://www.deviantart.com/?section=&global=1&q='

CHUNK_SIZE = 32768

import bs4, requests, os, sys

def imgSiteDownloadrer(keyword):
    os.makedirs(keyword, exist_ok=True)
    
    resp = requests.get(searchUrl + keyword)

    try:
        resp.raise_for_status()
    except Exception as exc:
        print('Error: {}'.format(exc))
        return

    soup = bs4.BeautifulSoup(resp.text, 'html5lib')
    #elem = soup.select('img')
    
    for elem in soup.select('img[data-sigil]'):
        #get img url
        imgResp = requests.get(elem['src'])

        try:
            imgResp.raise_for_status()
        except Exception as exc:
            print('{} is not accessable, skip.'.format(elem['src']))
            continue
        
        print('Downloading {}...'.format(os.path.basename(elem['src'])))
        with open(os.path.join(keyword, os.path.basename(elem['src'])), 'wb') as file:
            for chunk in imgResp.iter_content(CHUNK_SIZE):
                file.write(chunk)
        
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python imgSiteDownloader.py KEYWORD')
    else:
        imgSiteDownloadrer(sys.argv[1])