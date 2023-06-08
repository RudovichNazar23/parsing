import requests
import json
from bs4 import BeautifulSoup

res_json = []

for i in range(1, 6):
    for j in range(1, 5):
        url = f"https://parsinger.ru/html/index{i}_page_{j}.html"

        response = requests.get(url=url)
        response.encoding = "utf-8"

        soup = BeautifulSoup(response.text, "lxml")

        item_links = [i.find("a")["href"] for i in soup.find_all("div", attrs={"class": "sale_button"})]

        for item_link in item_links:
            url = f"https://parsinger.ru/html/{item_link}"
            response = requests.get(url=url)
            response.encoding = "utf-8"

            soup = BeautifulSoup(response.text, "lxml")

            name = soup.find("p", attrs={"id": "p_header"}).text
            article = soup.find("p", attrs={"class": "article"}).text.split(":")[1]
            description = soup.find("ul", attrs={"id": "description"}).find_all("li")
            count = soup.find("span", attrs={"id": "in_stock"}).text.split(":")[1]
            price = soup.find("span", attrs={"id": "price"}).text
            old_price = soup.find("span", attrs={"id": "old_price"}).text
            link = response.url

            res_json.append(
                {
                    "name": name,
                    "article": article,
                    "description": dict((el["id"], el.text.split(":")[1]) for el in description),
                    "count": count,
                    "price": price,
                    "old_price": old_price,
                    "link": link,
                }
            )
        with open("/home/nazar/Дакументы/all_stuff.json", "w", encoding="utf-8") as file:
            json.dump(res_json, file, indent=4, ensure_ascii=False)
