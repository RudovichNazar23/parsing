import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver import Keys

processed_spans = []

with webdriver.Chrome() as browser:
    browser.get(url="https://parsinger.ru/infiniti_scroll_1/")
    time.sleep(2)

    spans = [i for i in browser.find_element(By.ID, "scroll-container").find_elements(By.TAG_NAME, "span") if i not in processed_spans]

    while spans:
        for i in spans:
            if i not in processed_spans:
                i.find_element(By.TAG_NAME, "input").send_keys(Keys.DOWN)
                i.find_element(By.TAG_NAME, "input").click()
                processed_spans.append(i)
                time.sleep(2.5)

        spans = [i for i in browser.find_element(By.ID, "scroll-container").find_elements(By.TAG_NAME, "span") if i not in processed_spans]

    res = [int(i) for i in browser.find_element(By.ID, "scroll-container").text.split("\n")]

    print(sum(res))
