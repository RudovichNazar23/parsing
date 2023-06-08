import requests
import csv
from bs4 import BeautifulSoup

headers = (
    "Name", "Article", "Brand", "Model", "Type", "Screen Technology",
    "Frame Material", "Bracelet Material", "Size", "Site", "In stock",
    "Price", "Old Price", "Link"
)

with open("/home/nazar/Дакументы/watches.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(headers)

for i in range(1, 5):
    url = f"https://parsinger.ru/html/index1_page_{i}.html"
    response = requests.get(url=url)
    response.encoding = "utf-8"

    soup = BeautifulSoup(response.text, "lxml")

    links = [i.find("a")["href"] for i in soup.find_all("div", attrs={"class": "sale_button"})]

    for item_link in links:
        url = f"https://parsinger.ru/html/{item_link}"
        response = requests.get(url=url)
        response.encoding = "utf-8"

        soup = BeautifulSoup(response.text, "lxml")

        name = soup.find("p", attrs={"id": "p_header"}).text
        article = soup.find("p", attrs={"class": "article"}).text.split(":")[1]
        in_stock = soup.find("span", attrs={"id": "in_stock"}).text.split(":")[1]
        price = soup.find("span", attrs={"id": "price"}).text
        old_price = soup.find("span", attrs={"id": "old_price"}).text
        brand = soup.find("li", attrs={"id": "brand"}).text.split(":")[1]
        model = soup.find("li", attrs={"id": "model"}).text.split(":")[1]
        connection_type = soup.find("li", attrs={"id": "type"}).text.split(":")[1]
        display_technology = soup.find("li", attrs={"id": "display"}).text.split(":")[1]
        material_frame = soup.find("li", attrs={"id": "material_frame"}).text.split(":")[1]
        material_bracelet = soup.find("li", attrs={"id": "material_bracer"}).text.split(":")[1]
        size = soup.find("li", attrs={"id": "size"}).text.split(":")[1]
        site = soup.find("li", attrs={"id": "site"}).text.split(":")[1]
        link = response.url

        res = name, article, brand, model, connection_type, display_technology, material_frame, material_bracelet, \
            size, site, in_stock, price, old_price, link

        file = open("/home/nazar/Дакументы/watches.csv", "a", newline="", encoding="utf-8-sig")
        writer = csv.writer(file, delimiter=";")
        writer.writerow(res)
    file.close()


