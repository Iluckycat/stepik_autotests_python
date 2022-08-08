import unittest
from selenium import webdriver
import time
link = "http://suninjuly.github.io/registration2.html"

class TestAbs(unittest.TestCase):
    def test_1(self):
        browser = webdriver.Chrome('chromedriver.exe')
        browser.get(link)
        time.sleep(30)
        input1 = browser.find_element_by_tag_name(
            'form[action="registration_result.html"] .first_block .first_class input')
        input1.send_keys("Andrey")
        input2 = browser.find_element_by_tag_name(
            'form[action="registration_result.html"] .first_block .second_class input')
        input2.send_keys("Voronin")
        input3 = browser.find_element_by_tag_name(
            'form[action="registration_result.html"] .first_block .third_class input')
        input3.send_keys("Andrey@yrt")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Regisred is failed")
        browser.quit()
if __name__ == "__main__":
    unittest.main()