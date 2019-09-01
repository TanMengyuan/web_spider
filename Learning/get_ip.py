import requests

url = 'http://m.ip138.com/mobile.asp?mobile='
mobile = '13097215177'

try:
    r = requests.get(url+mobile)
    print(r.status_code)
    r.raise_for_status()
    print(r.text[-500:])
except:
    print('Fail.')

