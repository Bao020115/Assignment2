from pages.login_page import LoginPage
from utils.webdriver_setup import Driver
import time


class TestLogin(Driver):
    def test_logout(self, driver):
        login_Page = LoginPage(driver)
        email = "trangiabao256@gmail.com"
        password = "trunganh256"
        login_Page.go_to_login(email, password)
        time.sleep(5)
        login_Page.logout()
        assert driver.current_url == "http://localhost/opencart/index.php?route=account/logout&language=en-gb"

    def test_logout_without_login(self, driver):
        driver.get("http://localhost/opencart/index.php?route=account/logout&language=en-gb")
        assert driver.current_url != "http://localhost/opencart/"
        # lỗi web vì assert phải là != http://localhost/opencart/index.php?route=account/logout&language=en-gb




