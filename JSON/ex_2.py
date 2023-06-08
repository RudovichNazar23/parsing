import requests
from bs4 import BeautifulSoup
import json

res_json = []

for i in range(1, 6):
    for j in range(1, 5):
        url = f"https://parsinger.ru/html/index{i}_page_{j}.html"
        response = requests.get(url=url)
        response.encoding = "utf-8"

        soup = BeautifulSoup(response.text, "lxml")

        name = [x.text for x in soup.find_all("a", attrs={"class": "name_item"})]
        description = [x.text.strip().split("\n") for x in soup.find_all("div", attrs={"class": "description"})]
        price = [x.text for x in soup.find_all("p", attrs={"class": "price"})]

        for n, p, desc in zip(name, price, description):
            res_json.append(
                {
                    "name": n,
                    "brand": [x.split(":")[1] for x in desc][0],
                    "type": [x.split(":")[1] for x in desc][1],
                    "connection": [x.split(":")[1] for x in desc][2],
                    "game": [x.split(":")[1] for x in desc][3],
                    "price": p
                }
            )
    with open("/home/nazar/Дакументы/all_cats.json", "w", encoding="utf-8") as file:
        json.dump(res_json, file, ensure_ascii=False, indent=4)
