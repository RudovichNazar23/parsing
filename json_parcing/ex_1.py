import requests

url = "https://parsinger.ru/downloads/get_json/res.json"
response = requests.get(url=url).json()

print(response)

res = {
    "watch": 0,
    "mobile": 0,
    "mouse": 0,
    "hdd": 0,
    "headphones": 0,
}

for item in response:
    res["watch"] += int(item["count"]) if item["categories"] == "watch" else 0
    res["mobile"] += int(item["count"]) if item["categories"] == "mobile" else 0
    res["mouse"] += int(item["count"]) if item["categories"] == "mouse" else 0
    res["hdd"] += int(item["count"]) if item["categories"] == "hdd" else 0
    res["headphones"] += int(item["count"]) if item["categories"] == "headphones" else 0

print(res)
