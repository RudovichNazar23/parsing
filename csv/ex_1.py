import requests
import csv
from bs4 import BeautifulSoup

headers = [
    "Name", "Brand", "Form-factor", "Capacity", "Buf-memory", "Price"
]

with open("/home/nazar/Дакументы/plik.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(headers)

url = "https://parsinger.ru/html/index4_page_1.html"
response = requests.get(url=url)
response.encoding = "utf-8"

soup = BeautifulSoup(response.text, "lxml")

pagination_urls = [i["href"] for i in soup.find("div", attrs={"class": "pagen"}).find_all("a")]


for page in pagination_urls:
    url = f"https://parsinger.ru/html/{page}"
    response = requests.get(url=url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "lxml")

    names = [x.text.strip() for x in soup.find_all("a", attrs={"class": "name_item"})]
    description = [i.text.split("\n") for i in soup.find_all("div", attrs={"class": "description"})]
    price = [j.text for j in soup.find_all("p", attrs={"class": "price"})]

    for item, price, descr in zip(names, price, description):
        flatten = item, price, *[x.split(':')[1].strip() for x in descr if x]

        file = open('/home/nazar/Дакументы/plik.csv', 'a', encoding='utf-8-sig', newline='')
        writer = csv.writer(file, delimiter=';')
        writer.writerow(flatten)
    file.close()
