import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get(url="https://parsinger.ru/blank/modal/2/index.html")
    time.sleep(1.5)

    buttons = [i for i in browser.find_elements(By.TAG_NAME, "input")]

    for i in buttons:
        i.click()
        browser.switch_to.alert.accept()
        res = browser.find_element(By.ID, "result").text
        if res:
            print(int(res))
            break
        time.sleep(1)


