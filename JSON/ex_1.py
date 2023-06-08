import requests
from bs4 import BeautifulSoup
import json


result_json = []

for i in range(1, 5):
    url = f"https://parsinger.ru/html/index3_page_{i}.html"
    response = requests.get(url=url)
    response.encoding = "utf-8"

    soup = BeautifulSoup(response.text, "lxml")

    name = [x.text for x in soup.find_all("a", attrs={"class": "name_item"})]
    description = [x.text.strip().split("\n") for x in soup.find_all("div", attrs={"class": "description"})]
    price = [x.text for x in soup.find_all("p", attrs={"class": "price"})]

    for n, p, ds in zip(name, price, description):
        result_json.append(
            {
                "name": n,
                "brand": [x.split(":")[1] for x in ds][0],
                "type": [x.split(":")[1] for x in ds][1],
                "connection": [x.split(":")[1] for x in ds][2],
                "game": [x.split(":")[1] for x in ds][3],
                "price": p
            }
        )

with open("/home/nazar/Дакументы/res.json", "w", encoding="utf-8") as file:
    json.dump(result_json, file, indent=4, ensure_ascii=False)


