from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex_conditions

with webdriver.Chrome() as browser:
    browser.get(url="http://parsinger.ru/expectations/4/index.html")

    checking = WebDriverWait(browser, 10)
    checking.until(ex_conditions.element_to_be_clickable((By.ID, "btn"))).click()

    value = WebDriverWait(browser, 60).until(ex_conditions.title_contains("JK8HQ"))
    print(browser.title)

