import requests

url = 'https://item.jd.com/5762407.html'
try:
    r = requests.get(url)
    #检查返回代码是否异常：
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print('爬取失败')