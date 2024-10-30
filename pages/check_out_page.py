import time
from selenium.webdriver.common.by import By
from pages.home_page import NavigationPage
from utils.webdriver_setup import Driver


class CheckoutPage(Driver):
    def __init__(self, driver):
        self.driver = driver

    def go_to_checkout_page(self):
        NavigationPage(self.driver).go_to_home_page()
        self.driver.find_element(By.LINK_TEXT, "Checkout").click()
        time.sleep(1)

    def get_message(self):
        message = self.driver.find_element(By.XPATH, "/html/body/div/div").text
        return message

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def input_feilds(self, firstname, lastname, company, address1, adress2, city, postcode):
        self.driver.find_element(By.ID, "input-shipping-firstname").send_keys(firstname)
        time.sleep(2)
        self.driver.find_element(By.ID, "input-shipping-lastname").send_keys(lastname)
        time.sleep(2)
        self.driver.find_element(By.ID, "input-shipping-company").send_keys(company)
        time.sleep(2)
        self.driver.find_element(By.ID, "input-shipping-address-1").send_keys(address1)
        time.sleep(2)
        self.driver.find_element(By.ID, "input-shipping-address-2").send_keys(adress2)
        time.sleep(2)
        self.driver.find_element(By.ID, "input-shipping-city").send_keys(city)
        time.sleep(2)
        self.driver.find_element(By.ID, "input-shipping-postcode").send_keys(postcode)
        time.sleep(2)
        self.driver.find_element(By.XPATH,
                                 "/html/body/main/div[2]/div/div/div/div[1]/div/fieldset/div[3]/form/div[1]/div[8]/select/option[247]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,
                                 "/html/body/main/div[2]/div/div/div/div[1]/div/fieldset/div[3]/form/div[1]/div[9]/select/option[31]").click()
        time.sleep(2)
        self.scroll_to_element(self.driver.find_element(By.XPATH,
                                                        "/html/body/main/div[2]/div/div/div/div[1]/div/fieldset/div[3]/form/div[2]/button"))
        self.driver.find_element(By.XPATH,
                                 "/html/body/main/div[2]/div/div/div/div[1]/div/fieldset/div[3]/form/div[2]/button").click()
        time.sleep(2)

    def shipping_method(self):
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/button").click()
        self.scroll_to_element(self.driver.find_element(By.ID, "button-shipping-methods"))
        time.sleep(2)
        self.driver.find_element(By.ID, "button-shipping-methods").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div[1]/input").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div[2]/button").click()
        time.sleep(1)

    def payment_method(self):
        time.sleep(2)
        self.scroll_to_element(self.driver.find_element(By.XPATH,
                                                        "/html/body/main/div[2]/div/div/div/div[2]/div[2]/fieldset/div[1]/button"))
        time.sleep(2)
        self.driver.find_element(By.XPATH,
                                 "/html/body/main/div[2]/div/div/div/div[2]/div[2]/fieldset/div[1]/button").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[1]/input").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[2]/button").click()
        time.sleep(1)

    def comfirm_order(self):
        time.sleep(5)
        self.scroll_to_element(
            self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[2]/div[3]/div[2]/div/button"))
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[2]/div[3]/div[2]/div/button").click()
        time.sleep(5)

    def use_new_address(self):
        self.driver.find_element(By.XPATH,
                                 "/html/body/main/div[2]/div/div/div/div[1]/div/fieldset/div[1]/div[2]/input").click()
        time.sleep(3)

    def used_address(self):
        self.driver.find_element(self.driver.find_element(By.XPATH,
                                                          "/html/body/main/div[2]/div/div/div/div[1]/div/fieldset/div[2]/select/option[1]")).click()
        time.sleep(2)

    def get_error_input(self):
        # Use CSS_SELECTOR for multiple classes
        error_elements = self.driver.find_elements(By.CSS_SELECTOR, '.invalid-feedback.d-block')
        error_messages = [element.text for element in error_elements]

        # Add additional error if the specific XPath element exists
        if self.driver.find_elements(By.XPATH, "/html/body/main/div"):
            error_messages.append(self.driver.find_element(By.XPATH, "/html/body/main/div").text)

        return error_messages
