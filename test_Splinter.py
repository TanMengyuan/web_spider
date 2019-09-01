from splinter import Browser
browser = Browser()
# 指定driver为chrome浏览器
browser = Browser(driver_name='chrome')

browser.visit('http://baidu.com')