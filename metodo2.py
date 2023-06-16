import requests
from bs4 import BeautifulSoup
import json

link = 'https://www.ilsole24ore.com/art/dalla-certificazione-parita-welfare-tutte-misure-un-italia-piu-equa-AE5Yc7hD'

def get_whole_page(link: str) -> BeautifulSoup:
    res = requests.get(link)
    soup = BeautifulSoup(res.text, 'html.parser')

    return soup

def extract_article_json(page: BeautifulSoup) -> str:
    sgamo = page.find("script", class_="next-head").text
    return sgamo


page = get_whole_page(link=link)
json_string = extract_article_json(page=page)

json_page = json.loads(json_string)

for k, v in json_page.items():
    print(">>> ",k, ": ", v)

