import requests
from bs4 import BeautifulSoup

url = "https://parsinger.ru/table/3/index.html"

response = requests.get(url=url)
response.encoding = "utf-8"

soup = BeautifulSoup(response.text, "lxml")

nums = [float(i.text) for i in soup.find_all("b")]

res = 0

for num in nums:
    res += num

