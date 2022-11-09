import requests
import fake_useragent
from bs4 import BeautifulSoup

str_number = 1
img_number = 0
link = 'https://zastavok.net'



responce = requests.get(f'{link}/{str_number}').text
s = BeautifulSoup(responce, 'lxml')
block = s.find('div', class_ = 'block-photo')
all_image = block.find_all('div', class_ = 'short_full')

for image in all_image:
    image_link = image.find('a').get('href')
    download_storage = requests.get(f'{link}{image_link}').text
    download_soup = BeautifulSoup(download_storage, 'lxml')
    download_block = download_soup.find('div', class_ = 'image_data').find('div', class_='block_down')
    result_link = download_block.find('a').get('href')
    


    images_bytes = requests.get(f'{link}{result_link}').content
    

    with open(f'images/{img_number}.jpg', 'wb') as file:
        file.write(images_bytes)
    
    img_number += 1
    print(f'Изображение {img_number}. jpg успешно скачано')
