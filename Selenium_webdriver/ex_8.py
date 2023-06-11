from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get(url="https://parsinger.ru/selenium/6/6.html")
    nums = browser.find_elements(By.CLASS_NAME, "num")

    fr = int(nums[0].text[2:])
    sec_num = int(nums[1].text[0])
    thr_num = int(nums[2].text[0])
    on_num = int(nums[3].text)

    res = ((fr * sec_num) * thr_num) + on_num

    for i in browser.find_elements(By.TAG_NAME, "option"):
        if int(i.text) == res:
            i.click()
        continue
    browser.find_element(By.CLASS_NAME, "btn").click()
    print(browser.find_element(By.ID, "result").text)
