import requests
import time

for i in range(19):
    a = requests.get('https://movie.douban.com/top250')
    print(a)
    time.sleep(2)