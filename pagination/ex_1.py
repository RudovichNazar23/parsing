import requests
from bs4 import BeautifulSoup

url = "https://parsinger.ru/html/index3_page_1.html"

responsive = requests.get(url=url)
responsive.encoding = "utf-8"

soup = BeautifulSoup(responsive.text, "lxml")

links = soup.find("div", attrs={"class": "pagen"}).find_all("a")
names = soup.find_all("a", attrs={"class": "name_item"})
# print([i.text for i in names])

number_of_pages = [int(i.text) for i in links]

res = []

for i in number_of_pages:
    url = f"https://parsinger.ru/html/index3_page_{i}.html"

    response = requests.get(url=url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "lxml")
    names = soup.find_all("a", attrs={"class": "name_item"})
    res.append([i.text for i in names])

print(res)

