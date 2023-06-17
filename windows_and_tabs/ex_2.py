import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get(url="https://parsinger.ru/blank/modal/3/index.html")
    time.sleep(1.5)

    buttons = [
        i for i in browser.find_elements(By.TAG_NAME, "input")
    ]

    for b in buttons:
        b.click()
        number = browser.switch_to.alert.text
        browser.switch_to.alert.accept()

        browser.find_element(By.ID, "input").send_keys(number)
        browser.find_element(By.ID, "check").click()

        res = browser.find_element(By.ID, "result").text

        if res.isdigit():
            print(res)
            break
        time.sleep(1.5)
