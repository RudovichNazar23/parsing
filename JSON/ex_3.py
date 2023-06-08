import requests
import json
from bs4 import BeautifulSoup


res_json = []

for i in range(1, 5):
    url = f"https://parsinger.ru/html/index1_page_{i}.html"
    response = requests.get(url=url)
    response.encoding = "utf-8"

    soup = BeautifulSoup(response.text, "lxml")

    item_links = [i.find("a")["href"] for i in soup.find_all("div", attrs={"class": "sale_button"})]

    for item_link in item_links:
        url = f"https://parsinger.ru/html/{item_link}"
        response = requests.get(url=url)
        response.encoding = "utf-8"

        soup = BeautifulSoup(response.text, "lxml")

        category = soup.find()
        name = soup.find("p", attrs={"id": "p_header"}).text
        article = soup.find("p", attrs={"class": "article"}).text.split(":")[1]
        description = soup.find("ul", attrs={"id": "description"}).find_all("li")
        count = soup.find("span", attrs={"id": "in_stock"}).text.split(":")[1]
        price = soup.find("span", attrs={"id": "price"}).text
        old_price = soup.find("span", attrs={"id": "old_price"}).text
        link = response.url

        res_json.append(
            {
                "category": "",
                "name": name,
                "article": article,
                "description": {
                    "brand": description[0].text.split(":")[1],
                    "model": description[1].text.split(":")[1],
                    "type": description[2].text.split(":")[1],
                    "display": description[3].text.split(":")[1],
                    "material_frame": description[4].text.split(":")[1],
                    "material_bracer": description[5].text.split(":")[1],
                    "size": description[6].text.split(":")[1],
                    "site": description[7].text.split(":")[1],
                },
                "count": count,
                "price": price,
                "old_price": old_price,
                "link": link,
            }
        )
    with open("/home/nazar/Дакументы/all_cards.json", "w", encoding="utf-8") as file:
        json.dump(res_json, file, ensure_ascii=False, indent=4)
