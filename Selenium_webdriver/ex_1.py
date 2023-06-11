from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get(url="https://parsinger.ru/selenium/1/1.html")
    inputs = browser.find_elements(By.CLASS_NAME, "form")
    button = browser.find_element(By.CLASS_NAME, "btn")
    for field in inputs:
        field.send_keys("text")
    button.click()

    print(browser.find_element(By.ID, "result").text)
