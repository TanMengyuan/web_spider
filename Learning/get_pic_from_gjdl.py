import requests

path = 'E:/abc.jpg'
url = 'http://img0.dili360.com/rw9/ga/M01/49/2C/wKgBzFoL496AN9pkABTc9MA0ads452.tub.jpg'
r = requests.get(url)
print(r.status_code)
with open(path,'wb') as f:
    f.write(r.content)
    f.close()
    print('Save.')