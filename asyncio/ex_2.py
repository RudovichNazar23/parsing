import aiohttp
import asyncio
import requests
from bs4 import BeautifulSoup

site = "https://parsinger.ru/asyncio/create_soup/1/index.html"

res = []

links = []


def get_soup(url: str):
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, "lxml")

    return soup


def get_links(sp):
    domain = "https://parsinger.ru/asyncio/create_soup/1/"

    for i in sp.find_all("a", attrs={"class": "lnk_img"}):
        links.append(domain + str(i["href"]))
    return links


async def main(link, session):
    async with session.get(url=link) as response:
        if response.status == 200:
            txt = await response.text()
            elem = BeautifulSoup(txt, "lxml")
            res.append(int(elem.find("p", attrs={"class": "text"}).text))


async def run_tasks():
    async with aiohttp.ClientSession() as session:
        tasks = [main(link, session) for link in links]
        await asyncio.gather(*tasks)


soup = get_soup(url=site)
lnks = get_links(soup)

if __name__ == "__main__":
    asyncio.run(run_tasks())

print(sum(res))
