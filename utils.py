import os
import requests
from bs4 import BeautifulSoup

def soup_from_url(url: str, scrapingbee = False) -> BeautifulSoup:
    """
    Get BeautifulSoup object from a URL
    """
    if scrapingbee:
        response = requests.get(
            url='https://app.scrapingbee.com/api/v1/',
            params={
                'api_key': os.getenv('SCRAPINGBEE_API_KEY'),
                'url':url,
                'render_js': 'false',
            })
    else:
        response = requests.get(url)
    return BeautifulSoup(response.content, "html.parser")

def get_all_links_from_div(url: str, div: str = "LinksLevel_container__cGmmL", url_init: str = "https://www.kununu.com/de/") -> list:
    """
    Get all links from a div in the HTML corresponding to a URL
    """
    soup = soup_from_url(url).find(class_ = div)
    return [url_init + x["href"] for x in soup.find_all('a', href=True)]