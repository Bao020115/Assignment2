import time
from selenium.webdriver.common.by import By
from utils.webdriver_setup import Driver


class RegisPage(Driver):
    def __init__(self, driver):
        self.driver = driver

    def go_to_regis_page(self):
        self.driver.get("http://localhost/opencart/")
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/div/a/span").click()
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/div/ul/li[1]/a").click()
        time.sleep(2)

    def input_firstname(self, firstname):
        self.driver.find_element(By.ID, "input-firstname").send_keys(firstname)
        time.sleep(2)

    def input_lastname(self, lastname):
        self.driver.find_element(By.ID, "input-lastname").send_keys(lastname)
        time.sleep(2)

    def input_email(self, email):
        self.driver.find_element(By.ID, "input-email").send_keys(email)
        time.sleep(2)

    def input_password(self, password):
        self.driver.find_element(By.ID, "input-password").send_keys(password)
        time.sleep(2)

    def agree_privacy_policy(self):
        self.scroll_to_element(self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/form/div/div/input"))
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/form/div/div/input").click()
        time.sleep(2)

    def submit(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/form/div/button").click()
        time.sleep(2)

    def get_error_message(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/dirv").text

    def scroll_to_element(self, element):
        """Cuộn đến một phần tử cụ thể trên trang."""
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)

    # def error_firstname(self):
    #     return self.driver.find_element(By.ID, "input-firstname").get_attribute("validationMessage")
    #
    # def error_lastname(self):
    #     return self.driver.find_element(By.ID, "input-lastname").get_attribute("validationMessage")
    #
    # def error_email(self):
    #     return self.driver.find_element(By.ID, "input-email").get_attribute("validationMessage")
    #
    # def error_password(self):
    #     return self.driver.find_element(By.ID, "input-password").get_attribute("validationMessage")

    def get_error_input(self):
        error_elements = self.driver.find_elements(By.CLASS_NAME, 'invalid-feedback')
        error_messages = [element.text for element in error_elements]
        #  Nếu tồn tại self.driver.find_element(By.XPATH, "/html/body/div").text thì thêm vào error_messages
        if self.driver.find_elements(By.XPATH, "/html/body/div"):
            error_messages.append(self.driver.find_element(By.XPATH, "/html/body/div").text)

        return error_messages
