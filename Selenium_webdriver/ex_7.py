import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get(url="https://parsinger.ru/selenium/7/7.html")

    sm = sum([int(i.text) for i in browser.find_elements(By.TAG_NAME, "option")])
    time.sleep(5)
    browser.find_element(By.ID, "input_result").send_keys(sm)
    browser.find_element(By.CLASS_NAME, "btn").click()
    print(browser.find_element(By.TAG_NAME, "p").text)
