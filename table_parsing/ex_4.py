import requests
from bs4 import BeautifulSoup

url = "https://parsinger.ru/table/4/index.html"

response = requests.get(url=url)
response.encoding = "utf-8"

soup = BeautifulSoup(response.text, "lxml")

green_nums = [float(i.text) for i in soup.find_all("td", attrs={"class": "green"})]

res = 0

for i in green_nums:
    res += i
print(res)
