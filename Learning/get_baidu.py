import requests

r = requests.get('http://pg.njupt.edu.cn/')
r.encoding = r.apparent_encoding
print(r.text)