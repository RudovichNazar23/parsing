import time
from selenium import webdriver


from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


with webdriver.Chrome() as browser:
    browser.get(url="https://parsinger.ru/draganddrop/2/index.html")
    time.sleep(2.5)

    source_element = browser.find_element(By.ID, "draggable")

    targets = [i for i in browser.find_elements(By.CLASS_NAME, "box")]

    action = ActionChains(browser)

    for box in targets:
        action.drag_and_drop(source_element, box).perform()

        res = browser.find_element(By.ID, "message").text

        if res:
            print(res)

