from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time
driver = webdriver.Chrome('chromedriver.exe')
link = "http://suninjuly.github.io/explicit_wait2.html"
driver.get(link)
btn = driver.find_element_by_class_name("btn")
(WebDriverWait(driver,12).until(
    EC.text_to_be_present_in_element((By.ID,"price"),"100")))
btn.click()
input = int(driver.find_element_by_id("input_value").text)
result = math.log(abs(12*math.sin(input)))
answer = driver.find_element_by_id("answer")
answer.send_keys(result)
driver.find_element_by_id("solve").click()