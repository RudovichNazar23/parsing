import requests
from bs4 import BeautifulSoup


url = "https://parsinger.ru/table/5/index.html"

response = requests.get(url=url)
response.encoding = "urf-8"

soup = BeautifulSoup(response.text, "lxml")


cols = [x.text for x in soup.find_all("th")]
trs = soup.find_all("tr")[1:]

res = {}

for i in range(0, 65):
    for j in range(0, 15):
        res[f"{cols[j]}"] = sum([float(x.find_all("td")[j].text) for x in trs]).__round__(3)

print(res)

