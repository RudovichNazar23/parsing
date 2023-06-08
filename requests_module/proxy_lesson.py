import requests
from random import choice


url = 'http://httpbin.org/ip'


with open("../proxy.txt") as file:
    proxy_file = file.read().strip()
    for _ in range(10):
        try:
            ip = choice(proxy_file).strip()
            proxy = {
                "http": f"http://{ip}",
                "https": f"https://{ip}"
            }
            response = requests.get(url=url, headers=proxy)
            print(response.json(), "Success connection")
        except Exception as _ex:
            continue
