import requests
from bs4 import BeautifulSoup

url = "https://parsinger.ru/html/hdd/4/4_1.html"

response = requests.get(url=url)
response.encoding = "utf-8"

soup = BeautifulSoup(response.text, "lxml")

old_price = int(soup.find("span", attrs={"id": "old_price"}).text[:5])
new_price = int(soup.find("span", attrs={"id": "price"}).text[:5])

print(old_price)
print()
print(new_price)

discount = ((old_price - new_price) * 100 ) / old_price
print(discount)
