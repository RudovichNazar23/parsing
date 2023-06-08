import requests
from bs4 import BeautifulSoup

total = 0

index_labels = {1: "watch", 2: "mobile", 3: "mouse", 4: "hdd", 5: "headphones"}

for i in range(5):
    for j in range(32):
        url = f"https://parsinger.ru/html/{index_labels[i+1]}/{i+1}/{i+1}_{j+1}.html"
        response = requests.get(url=url)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, "lxml")
        res = int(soup.find("span", attrs={"id": "in_stock"}).text.split()[2]) * int(soup.find("span", attrs={"id": "price"}).text.split()[0])
        total += res

print(total)

