import time

from itertools import product
from selenium import webdriver
from selenium.webdriver.common.by import By

# options_chrome = webdriver.ChromeOptions()
# options_chrome.add_argument("--headless")

window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]


with webdriver.Chrome() as browser:
    browser.get(url="http://parsinger.ru/window_size/2/index.html")
    time.sleep(3)

    for x, y in product(window_size_x, window_size_y):
        browser.set_window_size(width=x + 44, height=y + 171)

        res = browser.find_element(By.ID, "result").text

        if res:
            print(res)
            time.sleep(5)
            break
        time.sleep(1)
