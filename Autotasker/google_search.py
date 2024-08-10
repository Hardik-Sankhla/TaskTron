import requests
from bs4 import BeautifulSoup

def google_search(query):
    search_url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = requests.get(search_url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []
        
        for g in soup.find_all('div', class_='tF2Cxc'):
            title = g.find('h3').text
            link = g.find('a')['href']
            results.append((title, link))
            
            if len(results) == 5:
                break
        
        return results
    else:
        return "Failed to retrieve search results"
