import requests
import fake_useragent
from bs4 import BeautifulSoup

str_number = 1

link = f'https://zastavok.net/{str_number}/'



responce = requests.get(link).text

s = BeautifulSoup(responce, 'lxml')
block = s.find('div', class_ = 'block-photo')
all_image = block.find_all('div', class_ = 'short_full')

for image in all_image:
    print(image)
    break
