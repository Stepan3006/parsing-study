import requests
import fake_useragent
from bs4 import BeautifulSoup

s = requests.Session()
data = {"login_username":"stepan@onepk.ru", "login_password":""}

url = 'https://stepik.org/learn?auth=login'

r = s.post(url, data=data)

print(s.cookies)

print(r)