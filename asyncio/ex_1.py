import aiohttp
import asyncio
import requests
from bs4 import BeautifulSoup

name_category = [
    "watch", "mobile", "mouse", "hdd", "headphones"
]

links = [
    f"https://parsinger.ru/html/{cat}/{i}/{i}_{x}.html" for cat, i in zip(name_category, range(1, len(name_category) + 1))
    for x in range(1, 33)
]

res = []


async def main(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            soup = BeautifulSoup(await resp.text(), "lxml")
            old_price = soup.find("span", attrs={"id": "old_price"}).text
            current_price = soup.find("span", attrs={"id": "price"}).text
            amount = soup.find("span", attrs={"id": "in_stock"}).text.split(":")[1]

            discount = (int(old_price.split(" ")[0]) - int(current_price.split(" ")[0])) * int(amount)

            res.append(
                discount
            )


async def run_tasks():
    tasks = [main(link) for link in links]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(run_tasks())

print(sum(res))
