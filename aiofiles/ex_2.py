import requests
import os
import aiohttp
import asyncio
import aiofiles
from bs4 import BeautifulSoup


links = []

images_links = []

ten_links = []


site = "https://parsinger.ru/asyncio/aiofile/3/index.html"


def get_links(url: str):
    domain = "https://parsinger.ru/asyncio/aiofile/3/"

    response = requests.get(url=url)

    soup = BeautifulSoup(response.text, "lxml")

    for i in soup.find_all("a", attrs={"class": "lnk_img"}):
        links.append(domain + i["href"])
    return links


async def get_ten_links(url, session):
    domain = "https://parsinger.ru/asyncio/aiofile/3/depth2/"

    async with session.get(url) as response:
        txt = await response.text()
        soup = BeautifulSoup(txt, "lxml")

        for link in soup.find_all("a", attrs={"class": "lnk_img"}):
            ten_links.append(domain + link["href"])
        return ten_links


async def get_src_images(link, session):
    async with session.get(link) as response:
        txt = await response.text()

        soup = BeautifulSoup(txt, "lxml")

        for x in soup.find_all("img", attrs={"class": "picture"}):
            if x["src"] not in images_links:
                images_links.append(x["src"])
        return images_links


async def write_image(link, session, name_image):
    async with aiofiles.open(f"/home/nazar/parcing/aiofiles/images/{name_image}", mode="wb") as file:
        async with session.get(link) as response:
            async for x in response.content.iter_chunked(1024):
                await file.write(x)


async def get_images():
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(write_image(link, session, link.split("/")[6])) for link in images_links]
        await asyncio.gather(*tasks)


async def run_ten_links():
    async with aiohttp.ClientSession() as session:
        tasks = [get_ten_links(link, session) for link in links]
        await asyncio.gather(*tasks)


async def run_get_src_images():
    async with aiohttp.ClientSession() as session:
        tasks = [get_src_images(link, session) for link in ten_links]
        await asyncio.gather(*tasks)


def get_folder_size(filepath, size=0):
    for root, dirs, files in os.walk(filepath):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
    return size


get_links(site)

if __name__ == '__main__':
    asyncio.run(run_ten_links())
    asyncio.run(run_get_src_images())
    asyncio.run(get_images())




