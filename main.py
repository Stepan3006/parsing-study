import requests
import fake_useragent
from bs4 import BeautifulSoup

s = requests.Session()
user = fake_useragent.UserAgent(use_cache_server=False).random()

header = {
    'user-agent':user
}
data = {"login_username":"stepan@onepk.ru", "login_password":""}

url = 'https://stepik.org/learn?auth=login'

r = s.post(url, data=data, headers=header).text

print(s.cookies)

print(r)