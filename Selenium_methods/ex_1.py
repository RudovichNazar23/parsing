from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get(url="https://parsinger.ru/methods/1/index.html")
    count = 30
    while count > 0:
        browser.refresh()
        res = browser.find_element(By.ID, "result").text
        try:
            int(res)
            count -= 1
            print(res)
        except Exception as e:
            count = 30

