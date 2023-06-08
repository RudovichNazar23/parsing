import requests
from bs4 import BeautifulSoup

url = "https://parsinger.ru/html/index3_page_4.html"

response = requests.get(url=url)
response.encoding = "utf-8"

soup = BeautifulSoup(response.text, "lxml")

pagination_links = [int(i.text) for i in soup.find("div", attrs={"class": "pagen"}).find_all("a")]

total = 0

for i in pagination_links:
    url = f"https://parsinger.ru/html/index3_page_{i}.html"
    response = requests.get(url=url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "lxml")
    sale_buttons = (i['href'] for i in soup.find_all('a', {'class': 'name_item'}))

    for j in sale_buttons:
        url = f"https://parsinger.ru/html/{j}"
        response = requests.get(url=url)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, "lxml")
        article = int(soup.find("p", attrs={"class": "article"}).text[9:])
        total += article
print(total)

