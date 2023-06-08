import csv
import requests
from bs4 import BeautifulSoup

lst = ["price", "form-factor", "brand"]

with open("/home/nazar/Дакументы/plik.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(lst)


url = "https://parsinger.ru/html/index4_page_1.html"

response = requests.get(url=url)
response.encoding = "utf-8"

soup = BeautifulSoup(response.text, "lxml")

price = soup.find("p", attrs={"class": "price"}).text.split(":")[0]

description = soup.find("div", attrs={"class": "description"}).find_all("li")

brand = description[0].text.split(":")[1]
form_factor = description[1].text.split(":")[1]

with open("/home/nazar/Дакументы/plik.csv", "a", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(
        [price, form_factor, brand]
    )




