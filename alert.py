from selenium import webdriver
import math
driver = webdriver.Chrome('chromedriver.exe')
link = "http://suninjuly.github.io/alert_accept.html"
driver.get(link)
driver.find_element_by_class_name("btn").click()
alert = driver.switch_to.alert
alert.accept()
input = int(driver.find_element_by_id("input_value").text)
result = math.log(abs(12*math.sin(input)))
answer = driver.find_element_by_id("answer")
answer.send_keys(result)
driver.find_element_by_class_name("btn").click()