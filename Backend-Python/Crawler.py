from bs4 import BeautifulSoup
import requests

def Crawler(target_url):
    try:
        res_urls = []
        res_pharagraps = []
        res_headers = []

        # crawling logic
        response = requests.get(target_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
        
            link_elements = soup.select("a[href]")
            for link_element in link_elements:
                url = link_element['href']
                if target_url in url:
                    if url not in res_urls:
                        res_urls.append(url)
            
            pharagraps = soup.select("p")
            for pharagrap in pharagraps:
                pharagrap = pharagrap.getText() if pharagrap else ""
                res_pharagraps.append(pharagrap)
                
            headers = soup.select("h1")
            for header in headers:
                header = header.getText() if header else ""
                res_headers.append(header)
            
            res_content = ("\n ".join(res_headers), "\n ".join(res_pharagraps))
            return [res_urls, res_content]
        else:
            return f"Failed to fetch URL. Status code: {response.status_code}"
    except Exception as e:
        return str(e)