from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get(url="https://parsinger.ru/selenium/3/3.html")

    vals = browser.find_elements(By.TAG_NAME, "p")
    res = 0

    for num in vals:
        res += int(num.text)
    print(res)
