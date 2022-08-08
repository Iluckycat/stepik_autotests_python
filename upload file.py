from selenium import webdriver
import os
driver = webdriver.Chrome('chromedriver.exe')
link = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(current_dir,'file.txt')

driver.get(link)
name = driver.find_element_by_name("firstname")
lastname = driver.find_element_by_name("lastname")
email = driver.find_element_by_name("email")
name.send_keys("Andrey")
lastname.send_keys("Voronin")
email.send_keys("andriei.voronin.2000@gmail.com")
upload_btn = driver.find_element_by_name("file")
upload_btn.send_keys(path)
btn = driver.find_element_by_class_name("btn")
btn.click()