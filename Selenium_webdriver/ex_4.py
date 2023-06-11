from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get(url="https://parsinger.ru/selenium/3/3.html")

    res = [int(i.text) for i in browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")]
    print(sum(res))




