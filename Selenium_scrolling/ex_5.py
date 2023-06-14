import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

with webdriver.Chrome() as browser:
    browser.get(url="https://parsinger.ru/infiniti_scroll_2/")
    time.sleep(1.5)

    div = browser.find_element(By.XPATH,
                               "//div[@style='width: 1px; height: 1px; visibility: hidden; position: absolute; top: 1500px;']")

    for i in range(10):
        ActionChains(browser).move_to_element(div).scroll_by_amount(1, 100).perform()
        time.sleep(2)
    time.sleep(3)

    res = [int(i.text) for i in browser.find_element(By.ID, "scroll-container").find_elements(By.TAG_NAME, "p") if i.text]
    print(sum(res))

