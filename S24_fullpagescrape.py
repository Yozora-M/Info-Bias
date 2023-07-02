import requests
from bs4 import BeautifulSoup
import json

#takes an url as input and gets the whole page
def get_whole_page(url: str) -> BeautifulSoup:
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    return soup

#extracts article data from whole page (get_whole_page)
def extract_article_json(page: BeautifulSoup) -> str:
    sgamo = page.find("script", class_="next-head").text
    return sgamo

#takes a base_url as input and returns all hrefs pointing to article pages
def get_all_article_hrefs(base_url: str):
    response = requests.get(base_url)

    soup = BeautifulSoup(response.text, "html.parser")

    elements = soup.find_all(class_="aprev-title")

    hrefs = []

    for element in elements:
        anchor = element.find("a")
        if anchor is not None:
            href = anchor.get("href")
            if not href.startswith("https"):
                href = base_url + href
                hrefs.append(href)
    
    return hrefs




base_url = "https://www.ilsole24ore.com"
article_urls = get_all_article_hrefs(base_url=base_url)
print(article_urls)

for url in article_urls:
    print("*"*99)
    print(f"getting {url} data ...")

    page = get_whole_page(url=url)
    
    json_string = extract_article_json(page=page)
    
    try:
        json_page = json.loads(json_string)
    except json.JSONDecodeError:
        print(f"@@@@ Error decoding page from {url}")

    for k, v in json_page.items():
        print(">>> ",k, ": ", v)

