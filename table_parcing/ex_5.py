import requests
from bs4 import BeautifulSoup


url = "https://parsinger.ru/table/5/index.html"

response = requests.get(url=url)
response.encoding = "utf-8"

soup = BeautifulSoup(response.text, "lxml")


blue_nums = [int(i.text) for i in soup.select("td:last-child")]
orange_nums = [float(i.text) for i in soup.find_all("td", attrs={"class": "orange"})]

res = 0

for i in range(0, len(blue_nums)):
    res += blue_nums[i] * orange_nums[i]

print(res)
