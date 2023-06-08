import requests

result = ""

for i in range(500):
    link_url = f"https://parsinger.ru/task/1/{str(i)}.html"
    req = requests.get(link_url, timeout=1)

    if req.status_code != 200:
        continue
    else:
        result = req.text
        break
