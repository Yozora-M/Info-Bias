import requests
from bs4 import BeautifulSoup

link = 'https://www.ilsole24ore.com/art/dalla-certificazione-parita-welfare-tutte-misure-un-italia-piu-equa-AE5Yc7hD'

def get_page_content(link: str) -> BeautifulSoup:
    res = requests.get(link)
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup
    
def extract_article_text(page: BeautifulSoup) -> str:
    p_atext = page.findAll("p", class_="atext")
    article_string = ""

    for p in p_atext:
        article_string += p.text
        article_string += "\n"

    return article_string

def extract_article_author(page: BeautifulSoup) -> str:
    p_auth = page.find("p", class_="auth").text
    return p_auth

def extract_article_title(page: BeautifulSoup) -> str:
    p_atitle = page.find("h1", class_="atitle").text
    return p_atitle


pagecontent = get_page_content(link=link)
text        = extract_article_text(pagecontent)
author      = extract_article_author(pagecontent)
title       = extract_article_title(pagecontent)

print(f"title:\n\n{title}")
print("\n\n")
print(f"author:\n\n{author}")
print("\n\n")
print(f"text:\n\n{text}")



