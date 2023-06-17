import time

from selenium import webdriver
from selenium.webdriver.common.by import By

res = []

with webdriver.Chrome() as browser:
    browser.get(url="https://parsinger.ru/blank/3/index.html")
    time.sleep(1)

    buttons = browser.find_elements(By.TAG_NAME, "input")

    for b in buttons:
        b.click()

    for x in range(len(browser.window_handles)):
        browser.switch_to.window(browser.window_handles[x])
        num = browser.execute_script("return document.title;")

        if num.isdigit():
            res.append(int(num))

print(sum(res))


