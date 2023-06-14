from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get(url="https://parsinger.ru/scroll/4/index.html")

    buttons = browser.find_elements(By.CLASS_NAME, "btn")

    res = 0

    for b in buttons:
        el = browser.execute_script(
            "return arguments[0].click();", b
        )
        res += int(browser.find_element(By.ID, "result").text)

print(res)
