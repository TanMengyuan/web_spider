import re

ls = re.findall(r'[1-9]\d{5}', '100081 100084')
if ls:
    print(ls)