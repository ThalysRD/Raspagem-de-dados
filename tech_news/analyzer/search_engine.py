from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    news = []
    for new in search_news({"title": {"$regex": title, "$options": "i"}}):
        news.append((new['title'], new['url']))
    return news


# Requisito 7
def search_by_date(date):
    news = []
    new_date = validate_date(date)
    for new in search_news({"timestamp": {"$regex": new_date}}):
        news.append((new['title'], new['url']))
    return news


# Requisito 8
def search_by_tag(tag):
    news = []
    for new in search_news({"tags": {"$regex": tag, "$options": "i"}}):
        news.append((new['title'], new['url']))
    return news


# Requisito 9
def search_by_category(category):
    news = []
    for new in search_news({"category": {"$regex": category,
                           "$options": "i"}}):
        news.append((new['title'], new['url']))
    return news


def validate_date(date):
    try:
        verify = datetime.strptime(date, "%Y-%m-%d")
        convert = verify.strftime("%d/%m/%Y")
    except ValueError:
        raise ValueError("Data inválida")
    return convert
