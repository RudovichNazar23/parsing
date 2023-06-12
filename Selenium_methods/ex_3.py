from selenium import webdriver


with webdriver.Chrome() as browser:
    browser.get(url="https://parsinger.ru/methods/3/index.html")

    cookies = [
        int(i["value"]) for i in browser.get_cookies() if int(i["name"].split("_")[2]) % 2 == 0
    ]
    print(sum(cookies))
