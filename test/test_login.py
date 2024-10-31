import time
from pages.login_page import LoginPage
from utils.webdriver_setup import Driver

class TestLogin(Driver):
    # login with valid information
    def test_login_with_valid_info(self, driver):
        login_Page = LoginPage(driver)
        email = "trangiabao256@gmail.com"
        password = "trunganh256"
        login_Page.go_to_login(email, password)
        assert driver.page_source.find("My Account") != -1
        time.sleep(5)
    # login with invalid information
    def test_login_with_invalid_info(self, driver):
        login_Page = LoginPage(driver)
        email = "trangiabao256@gmail"
        password = "trunganh256"
        login_Page.go_to_login(email, password)
        assert login_Page.get_error_message() == "Warning: No match for E-Mail Address and/or Password."
        time.sleep(5)
    # login with empty information
    def test_login_with_empty_info(self, driver):
        login_Page = LoginPage(driver)
        email = ""
        password = ""
        login_Page.go_to_login(email, password)
        assert login_Page.get_error_message() == "Warning: No match for E-Mail Address and/or Password."
        time.sleep(5)
    # login with invalid email
    def test_login_with_invalid_email(self, driver):
        login_Page = LoginPage(driver)
        email = "trangiabao256gmail.com"
        password = "trunganh256"
        login_Page.go_to_login(email, password)
        assert login_Page.get_error_message() == "Warning: No match for E-Mail Address and/or Password."
        time.sleep(5)
    # login with invalid password
    def test_login_with_invalid_password(self, driver):
        login_Page = LoginPage(driver)
        email = "trangiabao256@gmail.com"
        password = "trunganh"
        login_Page.go_to_login(email, password)
        assert login_Page.get_error_message() == "Warning: No match for E-Mail Address and/or Password."
        time.sleep(5)
    # login with empty email
    def test_login_with_empty_password(self, driver):
        login_Page = LoginPage(driver)
        email = "trangiabao256@gmail.com"
        password = ""
        login_Page.go_to_login(email, password)
        assert login_Page.get_error_message() == "Warning: No match for E-Mail Address and/or Password."
        time.sleep(5)
    # login with empty password
    def test_login_with_empty_email(self, driver):
        login_Page = LoginPage(driver)
        email = ""
        password = "trunganh256"
        login_Page.go_to_login(email, password)
        assert login_Page.get_error_message() == "Warning: No match for E-Mail Address and/or Password."
        time.sleep(5)

