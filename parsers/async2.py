import requests
import json
import aiohttp
import asyncio
from bs4 import BeautifulSoup


site = "https://parsinger.ru/html/index1_page_1.html"


class Parser:
    def __init__(self, site_link):
        self.url = site_link
        self._links_on_items = []
        self._name = []
        self._article = []
        self._price = []
        self._description = []
        self._old_price = []
        self._amount = []
        self._json_format = []

    def __add_to_result(self):
        for price, name, desc, art, old_pr, amn in zip(self._price, self._name, self._description, self._article, self._old_price, self._amount):
            self._json_format.append(
                {
                    "name": name,
                    "price": price,
                    "old-price": old_pr,
                    "article": art,
                    "brand": [i for i in desc][0],
                    "model": [i for i in desc][1],
                    "type_connection": [i for i in desc][2],
                    "screen_technology": [i for i in desc][3],
                    "material_frame": [i for i in desc][4],
                    "material_bracer": [i for i in desc][5],
                    "sizes": [i for i in desc][6],
                    "company_site": [i for i in desc][7],
                    "amount": amn
                }
            )

    def write(self):
        self.__add_to_result()

        with open("json_tr/res.json", "w", encoding="utf-8") as file:
            json.dump(self._json_format, file, indent=4, ensure_ascii=False)

    def get_links(self, url: str):
        domain = "https://parsinger.ru/html/"

        response = requests.get(url=url)

        soup = BeautifulSoup(response.text, "lxml")

        for i in soup.find_all("div", attrs={"class": "sale_button"}):
            self._links_on_items.append(domain + i.find("a")["href"])

        return self._links_on_items

    async def get_info_item(self, url: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                soup = BeautifulSoup(await response.text(), "lxml")

                name = soup.find("p", attrs={"id": "p_header"}).text
                article = soup.find("p", attrs={"class": "article"}).text.split(":")[1]
                description = [
                    i.text.split(":")[1] for i in soup.find("ul", attrs={"id": "description"}).find_all("li")
                ]
                amount = soup.find("span", attrs={"id": "in_stock"}).text.split(":")[1]
                price = soup.find("span", attrs={"id": "price"}).text
                old_price = soup.find("span", attrs={"id": "old_price"}).text

                self._name.append(
                    name
                )
                self._price.append(
                    price
                )
                self._description.append(
                    description
                )
                self._amount.append(amount)
                self._old_price.append(old_price)
                self._article.append(article)

    async def run_tasks(self):
        tasks = [self.get_info_item(link) for link in self._links_on_items]
        await asyncio.gather(*tasks)

    def __call__(self):
        self.get_links(self.url)
        asyncio.run(self.run_tasks())
        self.write()


if __name__ == '__main__':
    parser = Parser(site_link=site)
    parser()