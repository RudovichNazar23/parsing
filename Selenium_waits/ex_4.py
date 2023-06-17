from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex_conditions


with webdriver.Chrome() as browser:
    browser.get(url="http://parsinger.ru/expectations/6/index.html")

    check_button = WebDriverWait(browser, 10)
    check_button.until(ex_conditions.element_to_be_clickable((By.ID, "btn"))).click()

    search_elem = WebDriverWait(browser, 60).until(ex_conditions.presence_of_element_located((By.CLASS_NAME, "Y1DM2GR")))

    print(search_elem.text)

