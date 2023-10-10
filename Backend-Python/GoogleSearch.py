from googlesearch import search

def googleSearch(Keyword = ''):
    urls = []
    try:
        for r in search(Keyword, advanced=True):
            if r.url not in urls:
                urls.append(r.url)
        
        return urls
    except: 
        try:
            print("stoped, try to search again...")
            googleSearch(Keyword)
        except: 
            print('stoped, try start program manually')
