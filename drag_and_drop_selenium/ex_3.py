import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


with webdriver.Chrome() as browser:
    browser.get(url="https://parsinger.ru/draganddrop/3/index.html")
    time.sleep(2.5)

    source_element = browser.find_element(By.ID, "block1")

    action = ActionChains(browser)

    for i in range(0, 6):

        action.click_and_hold(source_element)
        action.move_by_offset(50, 0).perform()
        action.release().perform()

        res = browser.find_element(By.ID, "message").text
        if res:
            print(res)
        time.sleep(1.5)

