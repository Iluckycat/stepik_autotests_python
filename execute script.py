from selenium import webdriver
import math
driver = webdriver.Chrome('chromedriver.exe')
link = " http://SunInJuly.github.io/execute_script.html"
driver.get(link)
input = int(driver.find_element_by_id("input_value").text)
result = math.log(abs(12*math.sin(input)))
print(result)
answer = driver.find_element_by_id("answer")
answer.send_keys(result)
driver.find_element_by_id("robotCheckbox").click()
btn = driver.find_element_by_id("robotsRule")
driver.execute_script("return arguments[0].scrollIntoView(true);", btn)
btn.click()
driver.find_element_by_class_name("btn").click()