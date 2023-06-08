import requests
import csv
from bs4 import BeautifulSoup


with open("/home/nazar/Дакументы/all_data.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file, delimiter=";")


url = "https://parsinger.ru/html/index1_page_1.html"
response = requests.get(url=url)
response.encoding = "utf-8"

soup = BeautifulSoup(response.text, "lxml")

paginator_links = [i.text for i in soup.find("div", {"class": "pagen"})]

for i in range(1, 6):
    for x in range(1, 5):
        url = f"https://parsinger.ru/html/index{i}_page_{x}.html"
        response = requests.get(url=url)
        response.encoding = "utf-8"

        soup = BeautifulSoup(response.text, "lxml")

        name = [x.text for x in soup.find_all("a", attrs={"class": "name_item"})]
        description = [x.text.split("\n") for x in soup.find_all("div", attrs={"class": "description"})]
        price = [i.text for i in soup.find_all("p", attrs={"class": "price"})]

        for n, p, d in zip(name, price, description):
            res = n, p, *[x.split(":")[1] for x in d if x]

            file = open("/home/nazar/Дакументы/all_data.csv", "a", newline="", encoding="utf-8-sig")
            writer = csv.writer(file, delimiter=";")
            writer.writerow(res)








