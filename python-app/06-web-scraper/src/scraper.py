import requests
from bs4 import BeautifulSoup
import time

class WebScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def fetch_page(self, url):
        """Fetch a web page"""
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None
    
    def parse_html(self, html):
        """Parse HTML content"""
        return BeautifulSoup(html, 'html.parser')
    
    def extract_data(self, soup):
        """Extract data from parsed HTML"""
        data = []
        # Example: extract all links
        links = soup.find_all('a')
        for link in links:
            data.append({
                'text': link.get_text(strip=True),
                'href': link.get('href')
            })
        return data

if __name__ == '__main__':
    scraper = WebScraper('https://example.com')
    print("Scraper initialized")
