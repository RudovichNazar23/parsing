import time

from selenium import webdriver
from selenium.webdriver.common.by import By

sites = ['http://parsinger.ru/blank/1/1.html',
         'http://parsinger.ru/blank/1/2.html',
         'http://parsinger.ru/blank/1/3.html',
         'http://parsinger.ru/blank/1/4.html',
         'http://parsinger.ru/blank/1/5.html',
         'http://parsinger.ru/blank/1/6.html',
         ]


res = []

with webdriver.Chrome() as browser:
    for site in sites:
        browser.execute_script(f"window.open('{site}');")
        time.sleep(1.5)

    for tab in browser.window_handles[1:]:
        browser.switch_to.window(tab)

        browser.find_element(By.TAG_NAME, "input").click()
        res.append(int(browser.find_element(By.ID, "result").text) ** 0.5)

print(sum(res))
