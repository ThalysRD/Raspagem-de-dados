import requests
import time
from parsel import Selector


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
    content = Selector(html_content)
    news = content.css('a.cs-overlay-link::attr(href)').getall()
    if news:
        return news
    return []


# Requisito 3
def scrape_next_page_link(html_content):
    content = Selector(html_content)
    next_page = content.css('a.next::attr(href)').get()
    print(next_page)
    if next_page:
        return next_page
    return None


# Requisito 4
def scrape_news(html_content):
    content = Selector(html_content)
    string_sumary = '.entry-content > p:nth-of-type(1) *::text'
    url = content.css('link[rel=canonical]::attr(href)').get()
    title = str(content.css('h1.entry-title::text').get())
    timestamp = content.css('li.meta-date::text').get()
    writer = content.css('span.author a::text').get()
    incial_sumary = content.css(string_sumary).getall()
    summary = "".join(incial_sumary)
    category = content.css('span.label::text').get()
    tags = content.css('section.post-tags a::text').getall()
    comments_count = len(content.css('ol.comment-list li').getall())
    if tags is None:
        tags = []
    news = {
                'url': url,
                'title': title.strip(),
                'timestamp': timestamp,
                'writer': writer,
                'comments_count': comments_count,
                'summary': summary.strip(),
                'tags': tags,
                'category': category
            }

    return news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
