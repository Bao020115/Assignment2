import pages
from pages.home_page import NavigationPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time


class ShoppingCartPage:
    def __init__(self, driver):
        self.random_products = None
        self.driver = driver

    def go_to_shopping_cart_page(self):
        self.driver.get("http://localhost/opencart/index.php?route=checkout/cart&language=en-gb")
        time.sleep(1)

    def details_product_macbook(self):
        self.go_to_shopping_cart_page()
        pages.home_page.NavigationPage.home_page = NavigationPage(self.driver)
        pages.home_page.NavigationPage.home_page.go_to_all_laptops(self.driver)
        self.scroll_to_element(self.driver.find_element(By.LINK_TEXT, "MacBook"))
        self.driver.find_element(By.LINK_TEXT, "MacBook").click()
        time.sleep(1)

    def scroll_to_element(self, element):
        """Cuộn đến một phần tử cụ thể trên trang."""
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)

    def add_product_to_cart_macbook(self):
        pages.NavigationPage.home_page = NavigationPage(self.driver)
        pages.NavigationPage.home_page.go_to_all_desktops(self.driver)
        time.sleep(1)
        self.scroll_to_element(self.driver.find_element(By.XPATH,
                                                        "/html/body/main/div[2]/div/div/div[4]/div[5]/div/div[2]/form/div/button[1]"))
        self.driver.find_element(By.XPATH,
                                 "/html/body/main/div[2]/div/div/div[4]/div[5]/div/div[2]/form/div/button[1]").click()
        time.sleep(3)

    def quantity(self, quantity):
        self.driver.find_element(By.ID, "input-quantity").clear()
        self.driver.find_element(By.ID, "input-quantity").send_keys(quantity)
        time.sleep(1)

    def get_message(self):
        message = self.driver.find_element(By.XPATH, "/html/body/div/div").text
        return message

    def add_more_product(self):
        self.driver.find_element(By.ID, "button-cart").click()
        time.sleep(1)

    def search_product(self, productname):
        self.driver.find_element(By.XPATH, "/html/body/header/div/div/div[2]/div/input").send_keys(productname)
        self.driver.find_element(By.XPATH, "/html/body/header/div/div/div[2]/div/button").click()
        time.sleep(2)

    def go_back(self):
        self.driver.back()
        time.sleep(1)

    def clear_quantity(self):
        self.driver.find_element(By.ID, "input-quantity").clear()
        time.sleep(1)

    def remove_product(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[4]/form/div/button[2]").click()
        time.sleep(1)

    def update_product(self):
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div/table/tbody/tr/td[4]/form/div/input[1]").clear()
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div/table/tbody/tr/td[4]/form/div/input[1]").send_keys(random.randint(1, 10))
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div/table/tbody/tr/td[4]/form/div/button[1]").click()
        time.sleep(1)

    def button_label_macbook(self):
        self.scroll_to_element(self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[5]/div[1]/div/div[2]/form/div/button[1]"))
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[5]/div[1]/div/div[2]/form/div/button[1]").click()

    def button_label_air(self):
        self.scroll_to_element(self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[5]/div[2]/div/div[2]/form/div/button[1]"))
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[5]/div[2]/div/div[2]/form/div/button[1]").click()