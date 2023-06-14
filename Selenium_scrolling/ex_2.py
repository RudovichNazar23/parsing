import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

with webdriver.Chrome() as browser:
    browser.get(url="https://parsinger.ru/scroll/2/index.html")
    res = [

    ]

    inputs = browser.find_elements(By.TAG_NAME, "input")
    spans = browser.find_elements(By.TAG_NAME, "span")

    for inpt in inputs:
        inpt.click()
        res = [
            int(i.text) for i in spans if i.text
        ]
        inpt.send_keys(Keys.DOWN)
        time.sleep(1)

print(sum(res))

