import time
from twocaptcha import TwoCaptcha
from selenium import webdriver
from selenium.webdriver.common.by import By


def sender_solve(path):
    solver = TwoCaptcha("e355692c135ac6295260e6f37dbf7720")
    result = solver.normal(path)
    return result["code"]


with webdriver.Chrome() as browser:
    browser.get(url="https://captcha-parsinger.ru/?page=3")
    time.sleep(5)

    if 'Подтвердите, что вы не робот' in browser.page_source:
        browser.find_element(By.CSS_SELECTOR, 'div[class="chakra-form-control css-1sx6owr"]').find_element(By.TAG_NAME, 'img').screenshot('img.png')
        browser.find_element(By.ID, 'field-:r0:').send_keys(sender_solve('img.png'))
        browser.find_element(By.CSS_SELECTOR, 'button[class="chakra-button css-1wq39mj"]').click()

        time.sleep(3)

        containers = browser.find_element(By.CLASS_NAME, "main").find_elements(By.TAG_NAME, "div")

        for c in containers:
            print(c.find_element(By.TAG_NAME, "div").find_elements(By.TAG_NAME, "div")[1].find_element(By.CLASS_NAME, "css-lecvsm5").find_element(By.TAG_NAME, "ul").find_element(By.TAG_NAME, "li").text)
