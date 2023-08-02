import requests
import json
import aiohttp
import asyncio
from bs4 import BeautifulSoup

site = "https://parsinger.ru/html/index1_page_1.html"


class Parser:
    def __init__(self, site_url: str):
        self.site_url = site_url
        self._pagination_links = []
        self._items_links = []
        self._name = []
        self._price = []
        self._old_price = []
        self._amount = []
        self._article = []
        self._description = []
        self._res_to_json = []
        self._domain = site_url[:26]

    def __add_to_res_json(self):
        for name, price, old_price, amount, article, desc in zip(self._name, self._price, self._old_price, self._amount, self._article, self._description):
            self._res_to_json.append(
                {
                    "name": name,
                    "price": price,
                    "old-price": old_price,
                    "amount": amount,
                    "article": article,
                    "description": {

                    }
                }
            )

    def write(self):
        pass

    def get_pagination_links(self):
        response = requests.get(url=self.site_url)
        soup = BeautifulSoup(response.text, "lxml")

        for link in soup.find("div", attrs={"class": "pagen"}).find_all("a"):
            self._pagination_links.append(
                self._domain + link["href"]
            )
        return self._pagination_links

    async def get_items_links(self, url, session):
        async with session.get(url) as response:
            soup = BeautifulSoup(await response.text(), "lxml")

            for x in soup.find_all("div", attrs={"class": "sale_button"}):
                self._items_links.append(
                    self._domain + x.find("a")["href"]
                )

    async def get_item_info(self, url, session):
        async with session.get(url) as response:
            soup = BeautifulSoup(await response.text(), "lxml")

            name = soup.find("p", attrs={"id": "p_header"}).text
            article = soup.find("p", attrs={"class": "article"}).text.split(":")[1]
            description = [
                (i["id"], i.text.split(":")[1]) for i in soup.find("ul", attrs={"id": "description"}).find_all("li")
            ]
            amount = soup.find("span", attrs={"id": "in_stock"}).text.split(":")[1]
            price = soup.find("span", attrs={"id": "price"}).text
            old_price = soup.find("span", attrs={"id": "old_price"}).text

            self._name.append(name)
            self._article.append(article)
            self._amount.append(amount)
            self._price.append(price)
            self._old_price.append(old_price)
            self._description.append(description)

    async def run_get_items_links(self):
        async with aiohttp.ClientSession() as session:
            tasks = [self.get_items_links(link, session) for link in self._pagination_links]
            await asyncio.gather(*tasks)

    async def run_get_item_info(self):
        async with aiohttp.ClientSession() as session:
            tasks = [self.get_item_info(url, session) for url in self._items_links]
            await asyncio.gather(*tasks)

    def __call__(self):
        self.get_pagination_links()
        asyncio.run(self.run_get_items_links())
        asyncio.run(self.run_get_item_info())


if __name__ == '__main__':
    parser = Parser(site_url=site)
    parser()