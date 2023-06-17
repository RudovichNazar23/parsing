import time

from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get(url="http://parsinger.ru/blank/modal/4/index.html")
    time.sleep(2)

    pins = [i.text for i in browser.find_elements(By.TAG_NAME, "span")]

    for pin in pins:
        browser.find_element(By.ID, "check").click()
        browser.switch_to.alert.send_keys(pin)
        browser.switch_to.alert.accept()

        res = browser.find_element(By.ID, "result").text

        if res.isdigit():
            print(res)
            break
        time.sleep(1.5)
