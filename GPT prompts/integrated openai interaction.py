import difflib
import openai
import requests
from bs4 import BeautifulSoup

openai.api_key = "YOUR_API_KEY"

link = 'https://www.ilsole24ore.com/art/dalla-certificazione-parita-welfare-tutte-misure-un-italia-piu-equa-AE5Yc7hD'
link1 = 'https://www.ilsole24ore.com/art/dalla-certificazione-parita-welfare-tutte-misure-un-italia-piu-equa-AE5Yc7hD'

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

def extract_article_title(page: BeautifulSoup) -> str:
    p_atitle = page.find("h1", class_="atitle").text
    return p_atitle

def calcola_similarita(titolo1, titolo2):
    rapporto_similarita = difflib.SequenceMatcher(None, titolo1, titolo2).ratio()
    return rapporto_similarita

def generate_response(prompt):
    model_engine = "text-davinci-003"
    prompt = (f"{prompt}")

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

#contenuto articolo 1
titolo1 = extract_article_title(get_page_content(link=link))
testo1 = extract_article_text(get_page_content(link=link))

#contenuto articolo 2
titolo2 = extract_article_title(get_page_content(link=link1))
testo2= extract_article_text(get_page_content(link=link1))


article_titles = [titolo1, titolo2, "quant'altro", "quant'altro"]
article_text = [testo1,testo2,"quant'altro","quant'altro"]
article_numbers = len(article_titles)

for i in range(article_numbers - 1):
    percentuale_similarita = calcola_similarita(article_titles[i], article_titles[i+1])
    if percentuale_similarita >= 0.7:
        article1 = article_titles[i]
        article2 = article_titles[i+1]
        article1_content = article_text[i]
        article2_content = article_text[i+1]
        break
    else:
        continue

prompt = (f"Voglio che tu analizzi questi due articoli e crei un elenco puntato come riassunto della tematica trattata da entrambi e che riassuma i concetti chiave ed elementi principali in comune degli articoli elencati in un riassunto unico e comune per entrambi. Il sommario dovrà essere scritto in maniera consona all’enfasi (o assenza di essa) contenuta per evitare di creare un sommario che riporti i fatti in modo troppo neutrale e indifferente, dai enfasi ai contenuti nello stesso modo con cui sono redatti negli articoli, come se tu fossi lo scrittore di quegli articoli. Il riassunto deve contenere i punti principali della notizia ed il risultato finale deve essere un riassunto COMUNE per entrambi gli articoli. Il riassunto deve essere di 5 punti al massimo. Non aggiungere n.b. o note nella tua risposta ne tue spiegazioni finali.\n\nTesto articolo 1:  {article1_content} \n\nTesto articolo 2:  {article2_content}")
response = generate_response(prompt)

print(response)