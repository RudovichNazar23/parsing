import requests

import aiohttp
import aiofiles
import asyncio
import os
from bs4 import BeautifulSoup

links = []

site = "https://parsinger.ru/asyncio/aiofile/2/index.html"

src = []


def get_links(url: str):
    domain = "https://parsinger.ru/asyncio/aiofile/2/"

    response = requests.get(url=url)

    soup = BeautifulSoup(response.text, "lxml")

    for link in soup.find_all("a", attrs={"class": "lnk_img"}):
        links.append(str(domain) + str(link["href"]))
    return links


async def main(link, session):
    async with session.get(link) as response:
        txt = await response.text()

        soup = BeautifulSoup(txt, "lxml")

        for x in soup.find_all("img", attrs={"class": "picture"}):
            if x["src"] not in src:
                src.append(x["src"])


async def run_tasks():
    async with aiohttp.ClientSession() as session:
        tasks = [main(link, session) for link in links]
        await asyncio.gather(*tasks)


async def get_images():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for link in src:
            task = asyncio.create_task(write_image(link, session, link.split("/")[6]))
            tasks.append(task)
        await asyncio.gather(*tasks)


async def write_image(url, session, name_image):
    async with aiofiles.open(f"/home/nazar/parcing/aiofiles/images/{name_image}", mode="wb") as file:
        async with session.get(url) as response:
            async for x in response.content.iter_chunked(1024):
                await file.write(x)


def get_folder_size(filepath, size=0):
    for root, dirs, files in os.walk(filepath):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
    return size


get_links(url=site)

if __name__ == '__main__':
    asyncio.run(run_tasks())
    asyncio.run(get_images())

print(get_folder_size("/home/nazar/parcing/aiofiles/images/"))

