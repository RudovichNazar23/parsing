import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


with webdriver.Chrome() as browser:
    browser.get(url="https://parsinger.ru/scroll/3/")

    inputs = browser.find_elements(By.TAG_NAME, "input")
    spans = browser.find_elements(By.TAG_NAME, "span")

    lst = [
        *zip(inputs, spans)
    ]

    res = []

    for i in lst:
        i[0].send_keys(Keys.DOWN)
        i[0].click()
        if i[1].text:
            res.append(int(i[0].get_attribute("id")))


print(sum(res))
