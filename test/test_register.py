import time
from pages.resgis_page import RegisPage
from utils.webdriver_setup import Driver
from selenium.webdriver.common.by import By


class TestSubmission(Driver):
    def test_submission(self, driver):
        regis_page = RegisPage(driver)
        regis_page.go_to_regis_page()
        time.sleep(2)
        firstname = "test"
        lastname = "test"
        email = "test@gmail.com"
        password = "test"
        regis_page.input_firstname(firstname)
        regis_page.input_lastname(lastname)
        regis_page.input_email(email)
        regis_page.input_password(password)
        regis_page.agree_privacy_policy()
        regis_page.submit()
        time.sleep(2)
        assert "account/success" in driver.current_url

    def test_submission_with_invalid_info(self, driver):
        regis_page = RegisPage(driver)
        regis_page.go_to_regis_page()
        time.sleep(2)
        firstname = ""
        lastname = ""
        email = ""
        password = ""
        regis_page.input_firstname(firstname)
        regis_page.input_lastname(lastname)
        regis_page.input_email(email)
        regis_page.input_password(password)
        regis_page.agree_privacy_policy()
        regis_page.submit()
        time.sleep(2)
        assert "account/register" in driver.current_url

    def test_submission_without_agreeing(self, driver):
        regis_page = RegisPage(driver)
        regis_page.go_to_regis_page()
        time.sleep(2)
        firstname = "test"
        lastname = "test"
        email = "test@gmail.com"
        password = "test"
        regis_page.input_firstname(firstname)
        regis_page.input_lastname(lastname)
        regis_page.input_email(email)
        regis_page.input_password(password)
        regis_page.submit()
        time.sleep(2)
        assert driver.page_source.find("Warning: You must agree to the Privacy Policy!") != -1

    def test_submission_with_invalid_password(self, driver):
        regis_page = RegisPage(driver)
        regis_page.go_to_regis_page()
        time.sleep(2)
        firstname = "test"
        lastname = "test"
        email = "test@gmail.com"
        password = ""
        regis_page.input_firstname(firstname)
        regis_page.input_lastname(lastname)
        regis_page.input_email(email)
        regis_page.input_password(password)
        regis_page.agree_privacy_policy()
        regis_page.submit()
        time.sleep(2)
        assert driver.find_element(By.ID, "error-password").text == "Password must be between 4 and 20 characters!"

    def test_submission_with_used_email(self, driver):
        regis_page = RegisPage(driver)
        regis_page.go_to_regis_page()
        time.sleep(2)
        firstname = "test"
        lastname = "test"
        email = "test@gmail.com"
        password = "test"
        regis_page.input_firstname(firstname)
        regis_page.input_lastname(lastname)
        regis_page.input_email(email)
        regis_page.input_password(password)
        regis_page.agree_privacy_policy()
        regis_page.submit()
        time.sleep(2)
        assert "Warning: E-Mail Address is already registered!" in regis_page.get_error_message()

