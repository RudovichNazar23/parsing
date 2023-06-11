from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get(url="https://parsinger.ru/selenium/4/4.html")

    inputs = browser.find_elements(By.CLASS_NAME, "check")

    for check in inputs:
        check.click()
    browser.find_element(By.CLASS_NAME, "btn").click()
    print(browser.find_element(By.TAG_NAME, "p").text)

