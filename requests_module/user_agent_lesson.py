import requests
from random import choice

from fake_useragent import UserAgent

user_agent = UserAgent()

for _ in range(10):
    fake_ua = {"user-agent": user_agent.random}
    site = requests.get(url="https://google.com", headers=fake_ua)
    # print(site)


url = 'http://httpbin.org/user-agent'

with open('user_agent.txt') as file:
    lines = file.read().split('\n')

for _ in lines:
    user_agent = {'user-agent': choice(lines)}
    response = requests.get(url=url, headers=user_agent)
    # print(response.text)


