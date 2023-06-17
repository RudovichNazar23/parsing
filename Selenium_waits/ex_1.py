from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as check
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:
    browser.get(url="https://parsinger.ru/expectations/3/index.html")
    but = WebDriverWait(browser, 10)
    but.until(check.element_to_be_clickable((By.ID, "btn"))).click()

    elem = WebDriverWait(browser, 60)
    if elem.until(check.title_contains("345FDG3245SFD")):
        print(browser.find_element(By.ID, "result").text)




