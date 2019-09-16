import requests
from bs4 import BeautifulSoup
import re
import xlrd
import random
import time
import io
from selenium import webdriver

def get_cookies():
    url_log = 'http://www.qichacha.com/user_login'
    drive = webdriver.Chrome()
    drive.get(url_log)
    drive.find_element_by_id("nameNormal").clear()
    drive.find_element_by_id("nameNormal").send_keys("13097215177")
    drive.find_element_by_id("pwdNormal").clear()
    drive.find_element_by_id("pwdNormal").send_keys("")
    time.sleep(15)
    cookie_list = drive.get_cookies()
    cookie_dict = {}
    for cookie in cookie_list:
        cookie_dict[cookie['name']] = cookie['value']
    drive.quit()
    cookie_use = ''
    for key in cookie_dict:
        cookie_use = cookie_use + key + '=' + cookie_dict[key] + '; '
    # print(cookie_dict)
    cookie_use = cookie_use[:-2]
    return cookie_use

path = "E:\\sola\\tel-1.xlsx"
bk = xlrd.open_workbook(path)
shxrange = range(bk.nsheets)
sh = bk.sheet_by_name("Sheet1")
nrows = sh.nrows
ncols = sh.ncols
row_list = []

for i in range(0, nrows):
    row_data = sh.cell_value(i, 0)
    row_list.append(row_data)

url = "http://www.qichacha.com/search?key="
headers = {
    'Cookie' : get_cookies(),
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}

count = 0

for i in range(len(row_list)):
    exit_flag = False
    r = requests.get(url + row_list[i], headers= headers)# , proxies= get_random_ip(ip_list)
    demo = r.text
    soup = BeautifulSoup(demo, features='lxml')
    try:
        tel = soup.findAll('p', attrs={'class' : "m-t-xs"})[1]
    except:
        tel = ''
    pattern = re.compile(r'\d{3,4}-\d{7,8}|1{1}\d{10}')
    tel_num = re.findall(pattern, str(tel))
    print("company_name:", row_list[i])
    print(tel_num)
    rate = round((i / nrows) * 100, 2)
    print("rows =", i+1, ' ', rate, "% is already.")
    # if tel_num == []:
    #     count = count + 1
    #     if count > 5:
    #         exit_flag = True
    # else:
    #     count = 0
    if exit_flag:
        break
    time.sleep(5)
    if i % 30 == 0 & i != 0:
        time.sleep(20)

    with open('E:\\sola\\tel-add.txt', 'a') as fileWriter:
        fileWriter.write(row_list[i])
        fileWriter.write(str(tel_num))
        fileWriter.write('\n')