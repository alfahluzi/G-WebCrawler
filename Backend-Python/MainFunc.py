import Crawler 
import GoogleSearch 
import xlsxwriter


def _crawl(url, searched_link, result):
    content = ('','')
    if len(searched_link) <= 50:
        print('\n Num of Link:',len(searched_link))
        url = url.split("#")[0]
        if url not in searched_link:
            searched_link.append(url)
            print('================', url, '====================')
            crawRes = Crawler.Crawler(url)
            links = crawRes[0]
            content = crawRes[1]

            if type(content) is tuple and content != ('','') and content not in result:
                result.append(content)
                print('Data rechieved')

            for link in links:
                link = link.split('#')[0]
                if link not in searched_link:
                    if link not in ['F', 'I']:
                        print('Append', link)
                        searched_link.append(link)
                        
                        r = _crawl(link, searched_link, result)
                        if type(r[1]) is tuple and r[1] != ('','') and (r[1]) not in result:
                            result.append(r[1]) 
                            print('Data rechieved')

                        for x in r[0]:
                            if x not in searched_link:
                                print('Append', x)
                                searched_link.append(x)
                    else: print('Link not valid:',link)
                else: print('Link already crawled:',link)
        else: print('Link already crawled:',url)
    else: print('Reaching maximum link')
    return [searched_link, content, result]

def googleSearch(keyword, filename = 'result'):
    searched_link = []
    result = []
    urls = GoogleSearch.googleSearch(keyword)
    print('Google Search Result:')
    print("\n".join(urls))
    print('==========================\n')
    for url in urls:
        if len(searched_link) >= 50 : break
        if url not in searched_link:
            r = _crawl(url, searched_link, result)
            for x in r[0]:
                if x not in searched_link:
                    searched_link.append(x)
            if type(r[1]) is tuple and r[1] != ('','') and (r[1]) not in result:
                result.append(r[1])
                print('Data rechieved')
    print("\n============",'FINISH',"============")    
    print('Total result:', len(result))
    workbook = xlsxwriter.Workbook(f'{filename}.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', 'Header')
    worksheet.write('B1', 'Pharagraph')
    for i in range(len(result)):
        print(result[i])
        worksheet.write(f'A{i+2}', result[i][0])
        worksheet.write(f'B{i+2}', result[i][1])
    print("============",'FINISH',"============\n")    
    workbook.close()

def crawl(target_url):
    searched_link = []
    result = []
    if target_url not in searched_link:
        r = _crawl(target_url, searched_link, result)
        for x in r[0]:
            if x not in searched_link:
                searched_link.append(x)
        if type(r[1]) is tuple and r[1] != ('','') and (r[1]) not in result:
            result.append(r[1])
            print('Data rechieved')
    print("\n============",'FINISH',"============")    
    print('Total result:', len(result))
    for r in result:
        print(r)
    print("============",'FINISH',"============\n")    
    return result

googleSearch('Jokowi tiga periode', 'Jokowi tiga periode')
# crawl('https://www.geeksforgeeks.org/python-check-if-variable-is-tuple/')