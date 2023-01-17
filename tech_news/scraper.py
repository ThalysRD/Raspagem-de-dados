import requests
import time


# Requisito 1
def fetch(url):
    try:

        time.sleep(1)
        response = requests.get(url, timeout=3)
        status = response.status_code
        if status != 200:
            return None
    except requests.ReadTimeout:
        return None
    else:
        return response.text


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
