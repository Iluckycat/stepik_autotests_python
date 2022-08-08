from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://suninjuly.github.io/selects1.html')
num1 = driver.find_element_by_id('num1')
num2 = driver.find_element_by_id('num2')
result = int(num1.text) + int(num2.text)
print(result)
select = Select(driver.find_element_by_tag_name("select"))
select.select_by_value(str(result))
btn = driver.find_element_by_class_name("btn").click()