import requests, bs4, os

CHUNK_SIZE = 1000000

def downloadXkcd():
    os.makedirs('xkcd', exist_ok=True)
    
    url = 'https://xkcd.com/'
    
    while not url.endswith('#'):
        #Get page
        print('Downloading page %s...' % url)
        resp = requests.get(url)
        resp.raise_for_status()
        
        soup = bs4.BeautifulSoup(resp.text, 'html5lib')
        
        #Download comic
        elemComic = soup.select('#comic img')
        if elemComic == []:
            print('***Could not find comic image.***')
        else:
            try:
                comicUrl = 'http:' + elemComic[0].get('src')
                print('Downloading comic %s...' % comicUrl)
                ImgResp = requests.get(comicUrl)
                ImgResp.raise_for_status()
                
                with open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb') as file:
                    for chunk in ImgResp.iter_content(CHUNK_SIZE):
                        file.write(chunk)
            except requests.exceptions.MissingSchema:
                #skip this comic and move to previous comic
                print('***Could not download comic image, skip.***')
                prevLink = soup.select('a[rel="prev"]')[0]
                url = 'https://xkcd.com/' + prevLink.get('href')
                continue
            
        #move to previoud comic
        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'https://xkcd.com/' + prevLink.get('href')
        
        
                
    print('Done')

if __name__ == '__main__':
    downloadXkcd()