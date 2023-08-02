import requests
from bs4 import BeautifulSoup

url = "https://parsinger.ru/table/1/index.html"

response = requests.get(url=url)
response.encoding = "utf-8"

soup = BeautifulSoup(response.text, "lxml")

nums = {float(i.text) for i in soup.find_all("td")}

res = 0

for i in nums:
    res += i

print(res)
