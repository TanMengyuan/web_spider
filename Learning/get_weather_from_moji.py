# This is only a simple text about the use of Requests

import re
import requests
from datetime import datetime
from bs4 import BeautifulSoup

url = 'http://tianqi.moji.com/'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit'
                      '/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safar'
                      'i/537.36',
    }

r = requests.get(url, headers= headers)
print(r.text)
soup = BeautifulSoup(r.text, "html.parser")
temp = soup.find('div', attrs={'class': 'wea_weather clearfix'}).em.getText()
weather = soup.find('div', attrs={'class': 'wrap clearfix wea_info'}).b.getText()
sd = soup.find('div', attrs={'class': 'wea_about clearfix'}).span.getText()
print(temp, weather, sd)