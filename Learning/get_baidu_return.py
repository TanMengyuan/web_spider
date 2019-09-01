import requests

url = 'http://www.baidu.com/s'
keyword = 'Python'
try:
    kv = {'wd':keyword}
    r = requests.get(url, params = kv)
    print(r.status_code)
    r.raise_for_status()
    print(r.request.url)
    print(len(r.text))
except:
    print('Fail.')