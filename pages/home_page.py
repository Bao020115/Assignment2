import time
from selenium.webdriver.common.by import By
from utils.webdriver_setup import Driver


class NavigationPage(Driver):
    def __init__(self, driver):
        self.driver = driver
    # go to home page
    def go_to_home_page(self):
        self.driver.get("http://localhost/opencart/")
        time.sleep(3)
    # go to all desktops
    def go_to_all_desktops(self, driver):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[1]/a").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[1]/div/a").click()
        time.sleep(3)
    # go to all laptops
    def go_to_all_laptops(self, driver):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[2]/a").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[2]/div/a").click()
        time.sleep(3)
    # go to all components
    def go_to_all_components(self, driver):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[3]/a").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[3]/div/a").click()
        time.sleep(3)
    # go to all tablets
    def go_to_tablet(self, driver):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[4]/a").click()
        time.sleep(3)
    # go to all software
    def go_to_software(self, driver):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[5]/a").click()
        time.sleep(3)
    # go to all phones
    def go_to_phones(self, driver):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[6]/a").click()
        time.sleep(3)
    # go to all cameras
    def go_to_cameras(self, driver):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[7]/a").click()
        time.sleep(3)
    # go to shopping cart
    def go_to_shopping_cart(self, driver):
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[4]/a/span").click()
        time.sleep(3)
    # go to wishlist
    def go_to_wishlist(self, driver):
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[3]/a/span").click()
        time.sleep(3)
    # go to checkout
    def go_to_checkout(self, driver):
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[5]/a/span").click()
        time.sleep(3)
    # go to product details
    def go_to_product_details(self, driver):
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[2]/div[1]/div/div[1]/a/img").click()
        time.sleep(3)

    #scroll to element
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)