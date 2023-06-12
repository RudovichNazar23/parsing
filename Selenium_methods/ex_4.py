import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def data(lst: list):
    result = "0000-00-00"

    for d in lst:
        if d > result:
            result = d
        continue
    return result


with webdriver.Chrome() as browser:
    browser.get(url="https://parsinger.ru/methods/5/index.html")
    links = [
        i.get_attribute("href") for i in browser.find_elements(By.TAG_NAME, "a")
    ]
    cookies = {}
    dates = []
    for page in links:
        browser.get(url=page)
        date = time.strftime("%Y-%m-%d", time.localtime(browser.get_cookie("foo2")["expiry"]))
        dates.append(
            date
        )
        cookies[date] = page

    highest_date = data(dates)

    res_page = cookies[str(highest_date)]

    browser.get(url=res_page)
    print(browser.find_element(By.TAG_NAME, "p").text)





