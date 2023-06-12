from selenium import webdriver


with webdriver.Chrome() as browser:
    browser.get(url="https://parsinger.ru/methods/3/index.html")
    cookies = [
        int(i["value"]) for i in browser.get_cookies()
    ]
    print(sum(cookies))
