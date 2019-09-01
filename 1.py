import requests
from selenium import webdriver
import time

url = 'http://192.168.0.1'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'ecos_pw=1qw:language=cn; bLanguage=cn',
    'DNT': '1',
    'Host': '192.168.0.1',
    'If-Modified-Since': 'Thu Jan 01 00:00:00 1970',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}

drive = webdriver.Chrome()
drive.get(url)
time.sleep(5)
print(drive.find_element_by_id('statusWanIP'))
time.sleep(10)
drive.quit()
a = requests.get(url, headers=headers)
a.encoding = a.apparent_encoding
print(a.text)