import requests


proxy = {
     'http': 'socks5://D2Frs6:75JjrW@194.28.209.68:9925'
}

for i in range(1, 3):
    url = f"https://parsinger.ru/img_download/img/ready/{i}.png"
    response = requests.get(url=url, stream=True, proxies=proxy)
    with open(f"/home/nazar/Выявы/{i}.png", "wb") as photo:
        for _ in response:
            photo.write(response.content)

