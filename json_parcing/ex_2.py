import requests

url = "https://parsinger.ru/downloads/get_json/res.json"

response = requests.get(url=url).json()

res = {
    "watch": 0,
    "mobile": 0,
    "mouse": 0,
    "hdd": 0,
    "headphones": 0,
}


for item in response:
    for category in res.keys():
        res[category] += int(item["price"].split(" ")[0]) * int(item["count"]) if item["categories"] == category else 0

print(res)
