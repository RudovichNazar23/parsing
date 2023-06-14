from collections import deque

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


with webdriver.Chrome() as browser:
    browser.get(url="https://parsinger.ru/infiniti_scroll_3/")
    time.sleep(1.5)

    containers = []
    queue = deque()

    nums = []

    for i in range(1, 6):
        containers.append(browser.find_element(By.ID, f"scroll-container_{i}"))
        time.sleep(0.5)

    queue += containers

    while queue:
        container = queue.popleft()

        dynamic_div = container.find_element(By.TAG_NAME, "div")

        for i in range(9):
            ActionChains(browser).move_to_element(dynamic_div).scroll_by_amount(1, 1500).perform()
            time.sleep(1.5)

        nums.append([int(i) for i in container.text.split("\n") if i])
        time.sleep(1.5)

    res = [sum(i) for i in nums]
print(sum(res))
