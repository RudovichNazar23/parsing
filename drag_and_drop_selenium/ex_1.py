import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


with webdriver.Chrome() as browser:
    browser.get(url="https://parsinger.ru/draganddrop/1/index.html")
    time.sleep(3)

    source_element = browser.find_element(By.ID, "field1")

    target_element = browser.find_element(By.ID, "field2")

    action = ActionChains(browser)

    action.drag_and_drop(source_element, target_element).perform()

    print(browser.find_element(By.ID, "result").text)
