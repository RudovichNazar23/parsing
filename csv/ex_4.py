import requests
import csv
from bs4 import BeautifulSoup

headers = (
    "Name", "Article", "Brand", "Model", "In_stock", "Price", "Old Price", "Link"
)

with open("/home/nazar/Дакументы/all_stuff_info.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(headers)

for i in range(1, 6):
    for j in range(1, 5):
        url = f"https://parsinger.ru/html/index{i}_page_{j}.html"
        response = requests.get(url=url)
        response.encoding = "utf-8"

        soup = BeautifulSoup(response.text, "lxml")
        item_links = [i.find("a")["href"] for i in soup.find_all("div", attrs={"class": "sale_button"})]

        for item in item_links:
            url = f"https://parsinger.ru/html/{item}"
            response = requests.get(url=url)
            response.encoding = "utf-8"

            soup = BeautifulSoup(response.text, "lxml")

            name = soup.find("p", attrs={"id": "p_header"}).text
            article = soup.find("p", attrs={"class": "article"}).text.split(":")[1]
            model = soup.find("li", attrs={"id": "model"}).text.split(":")[1]
            brand = soup.find("li", attrs={"id": "brand"}).text.split(":")[1]
            in_stock = soup.find("span", attrs={"id": "in_stock"}).text.split(":")[1]
            price = soup.find("span", attrs={"id": "price"}).text
            old_price = soup.find("span", attrs={"id": "old_price"}).text
            link = response.url

            res = name, article, brand, model, in_stock, price, old_price, link

            file = open("/home/nazar/Дакументы/all_stuff_info.csv", "a", newline="", encoding="utf-8-sig")
            writer = csv.writer(file, delimiter=";")
            writer.writerow(res)
file.close()

