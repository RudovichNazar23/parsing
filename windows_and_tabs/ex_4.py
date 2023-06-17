import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get(url="http://parsinger.ru/window_size/1/")
    time.sleep(1.5)

    browser.set_window_size(width=555 + 44, height=555 + 171)
    time.sleep(10)

    print(browser.find_element(By.ID, "result").text)

