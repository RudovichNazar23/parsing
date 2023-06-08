import requests
from bs4 import BeautifulSoup

url = "https://parsinger.ru/html/index1_page_1.html"

response = requests.get(url=url)
response.encoding = "utf-8"

soup = BeautifulSoup(response.text, "lxml")

prices = soup.find_all("p", attrs={"class": "price"})

values = [int(i.text[:5]) for i in prices]


def sum_elem(lst: list):
    if not lst:
        return 0
    else:
        return lst[0] + sum_elem(lst[1:])


print(sum_elem(values))
