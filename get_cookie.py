from selenium import webdriver
import time

def get_cookies():
    url = 'http://www.qichacha.com/user_login'
    #service_args 可以传入phantomjs 的参数，这里是ssl认证
    drive = webdriver.Chrome()
    drive.get(url)
    drive.find_element_by_id("normalLogin").click()
    drive.find_element_by_id("nameNormal").clear()
    drive.find_element_by_id("nameNormal").send_keys("13097215177")
    drive.find_element_by_id("pwdNormal").clear()
    drive.find_element_by_id("pwdNormal").send_keys("asd19941016")
    #截图登录界面，获取到验证码
    #这一步很重要，需要等待phantomjs 加载完再去取得cookies
    time.sleep(20)
    cookie_list = drive.get_cookies()
    cookie_dict = {}
    for cookie in cookie_list:
        cookie_dict[cookie['name']] = cookie['value']
    drive.quit()
    # print(cookie_dict)
    return cookie_dict

if __name__ == '__main__':

    cookie = get_cookies()
    print(cookie)
    cookie_use = ''
    for key in cookie:
        cookie_use = cookie_use + key + '=' + cookie[key] + '; '
    cookie_use = cookie_use[:-2]
    print(cookie_use)
    print(type(cookie_use))