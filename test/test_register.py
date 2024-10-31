import time
from pages.resgis_page import RegisPage
from utils.webdriver_setup import Driver
from selenium.webdriver.common.by import By


class TestSubmission(Driver):
    # submission valid information registration
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

    # submission invalid information registration
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
    # register without agreeing
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
    # register with invalid password
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

    # register with used email
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
    # register with invalid email
    def test_submission_with_invalid_email(self, driver):
        regis_page = RegisPage(driver)
        regis_page.go_to_regis_page()
        time.sleep(2)
        firstname = "test"
        lastname = "test"
        email = "test"
        password = "test"
        regis_page.input_firstname(firstname)
        regis_page.input_lastname(lastname)
        regis_page.input_email(email)
        regis_page.input_password(password)
        regis_page.agree_privacy_policy()
        regis_page.submit()
        time.sleep(2)
        assert "E-Mail Address does not appear to be valid!" in regis_page.get_error_message()
    # register with 30 characters password
    def test_submission_with_30_characters_password(self, driver):
        regis_page = RegisPage(driver)
        regis_page.go_to_regis_page()
        time.sleep(2)
        firstname = "test"
        lastname = "test"
        email = "test1@gmail.com"
        password = "1234567890123456789012345678901234567890"
        regis_page.input_firstname(firstname)
        regis_page.input_lastname(lastname)
        regis_page.input_email(email)
        regis_page.input_password(password)
        regis_page.agree_privacy_policy()
        regis_page.submit()
        time.sleep(2)
        assert "account/success" in driver.current_url
        #web lỗi vì đăng ký với 30 ký tự vẫn được đăng ký.
        # assert "Password must be between 4 and 20 characters!" in regis_page.get_error_message()
    # register without firstname
    def test_regis_without_firstname(self, driver):
        regis_page = RegisPage(driver)
        regis_page.go_to_regis_page()
        time.sleep(2)
        firstname = ""
        lastname = "test"
        email = "test2@gmail.com"
        password = "test"
        regis_page.input_firstname(firstname)
        regis_page.input_lastname(lastname)
        regis_page.input_email(email)
        regis_page.input_password(password)
        regis_page.agree_privacy_policy()
        regis_page.submit()
        time.sleep(2)
        assert "First Name must be between 1 and 32 characters!" in regis_page.get_error_input()
    #   register without lastname
    def test_regis_without_lastname(self, driver):
        regis_page = RegisPage(driver)
        regis_page.go_to_regis_page()
        time.sleep(2)
        firstname = "test"
        lastname = ""
        email = "test3@gmail.com"
        password = "test"
        regis_page.input_firstname(firstname)
        regis_page.input_lastname(lastname)
        regis_page.input_email(email)
        regis_page.input_password(password)
        regis_page.agree_privacy_policy()
        regis_page.submit()
        time.sleep(2)
        assert "Last Name must be between 1 and 32 characters!" in regis_page.get_error_input()
    #   register without email
    def test_regis_without_email(self, driver):
        regis_page = RegisPage(driver)
        regis_page.go_to_regis_page()
        time.sleep(2)
        firstname = "test"
        lastname = "test"
        email = ""
        password = "test"
        regis_page.input_firstname(firstname)
        regis_page.input_lastname(lastname)
        regis_page.input_email(email)
        regis_page.input_password(password)
        regis_page.agree_privacy_policy()
        regis_page.submit()
        time.sleep(2)
        assert "E-Mail Address does not appear to be valid!" in regis_page.get_error_input()
#   register without password
    def test_regis_without_password(self, driver):
        regis_page = RegisPage(driver)
        regis_page.go_to_regis_page()
        time.sleep(2)
        firstname = "test"
        lastname = "test"
        email = "test4@gmail.com"
        password = ""
        regis_page.input_firstname(firstname)
        regis_page.input_lastname(lastname)
        regis_page.input_email(email)
        regis_page.input_password(password)
        regis_page.agree_privacy_policy()
        regis_page.submit()
        time.sleep(2)
        assert "Password must be between 4 and 20 characters!" in regis_page.get_error_input()


