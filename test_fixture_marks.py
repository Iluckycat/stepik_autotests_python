import pytest_parametrize
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/"

@pytest_parametrize.fixture(scope="function")
def browser():
    print("\nstart browser for test...")
    driver = webdriver.Chrome("chromedriver.exe")
    yield driver
    print("\nquit browser...")
    driver.quit()

class TestMainPage1():
    @pytest_parametrize.mark.skip
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
    @pytest_parametrize.mark.smoke
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
    @pytest_parametrize.mark.xfail
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "input.btn.btn-default")
    @pytest_parametrize.mark.xfail(reason="fixing this bug right now")
    def test_2_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "button.favorite")