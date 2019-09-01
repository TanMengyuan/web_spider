from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://192.168.168.168/0.htm")
driver.find_element_by_id("username").click()
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("121101701033300")
driver.find_element_by_id("password").click()
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("165412")
driver.find_element_by_id("submit").click()