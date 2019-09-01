import requests

url = 'http://pg.njupt.edu.cn/'#https://www.amazon.cn/gp/product/B01M8L5Z3Y
#修改headers，将Python的头部换成浏览器的头部
kv = {'user-agent':'Mozilla/5.0'}
try:
    r = requests.get(url, headers = kv)
    print(r.request.headers)
    #检查返回代码是否异常：
    print(r.status_code)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print('爬取失败')