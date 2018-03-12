import requests, bs4, os, threading

CHUNK_SIZE = 1000000

def downloadXkcd(startNum, endNum):
    os.makedirs('xkcd', exist_ok=True)
    
    for num in range(startNum, endNum):
        resp = requests.get('https://xkcd.com/%s' % num)
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
                continue
                
    print('Comic {} to {}, Done'.format(startNum, endNum))

if __name__ == '__main__':
    downloadThreads = []
    for i in range(0, 100, 10):
        thread = threading.Thread(target=downloadXkcd, args=(i, i+10))
        downloadThreads.append(thread)
        thread.start()
        
    for thread in downloadThreads:
        thread.join()
        
    print('All tasks done.')
        