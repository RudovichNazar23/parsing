import requests
from bs4 import BeautifulSoup

url = "https://parsinger.ru/table/2/index.html"

# response = requests.get(url=url)
# response.encoding = "utf-8"
#
# soup = BeautifulSoup(response.text, "lxml")

# f_column = [float(i.text) for i in soup.find_all("tr")[1].find_all("td")]
#
# res = 0
#
# for i in f_column:
#     res += i
#
# # print(res)


# td = [float(x.find('td').text) for x in soup.find_all('tr') if x.find('td')]

for i in range(0, 15):
    print(i)
