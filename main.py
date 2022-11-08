import requests

link = 'https://icanhazip.com/'
responce = requests.get(link).text

responce = requests.get(link).content
