import json

import requests
import aiohttp
import asyncio
from bs4 import BeautifulSoup

site_url = "https://knigorai.com/"


class Parser:
    def __init__(self, url: str):
        self.errors = []

        self._site = url
        self._pagination_links = []
        self._book_link = []

        self._name = []
        self._author = []
        self._author_link = []
        self._genre = []
        self._date_release = []
        self._reader = []
        self._reader_link = []
        self._book_duration = []

        self._res_to_json = []

    def get_pagination_links(self):
        return self._pagination_links

    def get_books_links(self):
        return self._book_link

    def collect_pagination_links(self):
        response = requests.get(url=self._site)
        soup = BeautifulSoup(response.text, "lxml")

        for link in soup.find("ul", attrs={"class": "pagination"}).find_all("li"):
            try:
                self._pagination_links.append(
                    self._site + link.find("a")["href"]
                )
            except Exception as error:
                continue

    def __to_json_format(self):
        for name, author, author_link, genre, date_release, reader, reader_link, book_duration in \
                zip(self._name, self._author, self._author_link, self._genre, self._date_release, self._reader,
                    self._reader_link, self._book_duration):
            self._res_to_json.append(
                {
                    "name": name,
                    "author": author,
                    "author_link": author_link,
                    "genre": genre,
                    "date_release": date_release,
                    "reader": reader,
                    "reader_link": reader_link,
                    "book_duration": book_duration
                }
            )

    def write_to_json(self):
        self.__to_json_format()

        with open("json_tr/res.json", "w", encoding="utf-8") as file:
            json.dump(self._res_to_json, file, indent=4, ensure_ascii=False)

    async def collect_book_link(self, url, session):
        async with session.get(url) as response:
            async_soup = BeautifulSoup(await response.text(), "lxml")

            for book_link in async_soup.find_all("div", attrs={"class": "media-left"}):
                try:
                    self._book_link.append(book_link.find("a")["href"])
                except Exception as error:
                    continue

    async def collect_book_info(self, book_url: str, session):
        async with session.get(book_url) as response:
            async_soup = BeautifulSoup(await response.text(), "lxml")

            try:
                name = async_soup.find("h1", attrs={"itemprop": "name"}).text
                author = async_soup.find("h2", attrs={"class": "book-author"}).find("a").text
                author_link = async_soup.find("h2", attrs={"class": "book-author"}).find("a")["href"]
                genre = async_soup.find("div", attrs={"class": "book-genres"}).find("div").find("a").text
                date_release = async_soup.find("div", attrs={"class": "book-year"}).find("div").find("a").text
                person_reads = async_soup.find("div", attrs={"class": "book-reader"}).find("div").find("a").text
                person_reads_link = async_soup.find("div", attrs={"class": "book-reader"}).find("div").find("a")["href"]
                time = async_soup.find("div", attrs={"class": "book-duration"}).find("div").text

                self._name.append(name), self._author.append(author), self._author_link.append(author_link)
                self._genre.append(genre), self._date_release.append(date_release), self._reader.append(person_reads)
                self._reader_link.append(person_reads_link), self._book_duration.append(time)

            except Exception as error:
                self.errors.append(error)

    async def run(self, func, links: list):
        async with aiohttp.ClientSession() as session:
            tasks = [func(link, session) for link in links]
            await asyncio.gather(*tasks)

    def __call__(self):
        self.collect_pagination_links()
        asyncio.run(self.run(self.collect_book_link, self._pagination_links))
        asyncio.run(self.run(self.collect_book_info, self._book_link))
        self.write_to_json()


if __name__ == '__main__':
    parser = Parser(url=site_url)
    parser()