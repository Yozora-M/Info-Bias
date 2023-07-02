import requests
from bs4 import BeautifulSoup

url = "https://www.ilsole24ore.com"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all the elements with class "aprev-title"
elements = soup.find_all(class_="aprev-title")

# Iterate through the elements
for element in elements:
    # Find the <a> tag within the element
    anchor = element.find("a")
    if anchor is not None:
        href = anchor.get("href")
        if not href.startswith("https"):
            href = url + href
        
        print(href)

