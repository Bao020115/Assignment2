import time

from pages.home_page import NavigationPage
from utils.webdriver_setup import Driver
from selenium.webdriver.common.by import By

class TestNavigation(Driver):
    # navigate to all desktop
    def test_navigate_to_desktop(self,driver):
        home_page = NavigationPage(driver)
        home_page.go_to_home_page()
        time.sleep(2)
        home_page.go_to_all_desktops(driver)
        time.sleep(2)
        assert driver.current_url == "http://localhost/opencart/index.php?route=product/category&language=en-gb&path=20"
    # navigate to all laptop
    def test_navigate_to_laptop(self,driver):
        home_page = NavigationPage(driver)
        home_page.go_to_home_page()
        time.sleep(2)
        home_page.go_to_all_laptops(driver)
        time.sleep(2)
        assert driver.current_url == "http://localhost/opencart/index.php?route=product/category&language=en-gb&path=18"
    # navigate to all components
    def test_navigate_to_component(self,driver):
        home_page = NavigationPage(driver)
        home_page.go_to_home_page()
        time.sleep(2)
        home_page.go_to_all_components(driver)
        time.sleep(2)
        assert driver.current_url == "http://localhost/opencart/index.php?route=product/category&language=en-gb&path=25"
    # navigate to all tablet
    def test_navigate_to_tablet(self,driver):
        home_page = NavigationPage(driver)
        home_page.go_to_home_page()
        time.sleep(2)
        home_page.go_to_tablet(driver)
        time.sleep(2)
        assert driver.current_url == "http://localhost/opencart/index.php?route=product/category&language=en-gb&path=57"
    # navigate to all software
    def test_navigate_to_software(self,driver):
        home_page = NavigationPage(driver)
        home_page.go_to_home_page()
        time.sleep(2)
        home_page.go_to_software(driver)
        time.sleep(2)
        assert driver.current_url == "http://localhost/opencart/index.php?route=product/category&language=en-gb&path=17"

    # navigate to all phones
    def test_navigate_to_phones(self,driver):
        home_page = NavigationPage(driver)
        home_page.go_to_home_page()
        time.sleep(2)
        home_page.go_to_phones(driver)
        time.sleep(2)
        assert driver.current_url == "http://localhost/opencart/index.php?route=product/category&language=en-gb&path=19"
    # navigate to all cameras
    def test_navigate_to_cameras(self,driver):
        home_page = NavigationPage(driver)
        home_page.go_to_home_page()
        time.sleep(2)
        home_page.go_to_cameras(driver)
        time.sleep(2)
        assert driver.current_url == "http://localhost/opencart/index.php?route=product/category&language=en-gb&path=33"
    # navigate to shopping cart
    def test_navigate_to_shopping_cart(self,driver):
        home_page = NavigationPage(driver)
        home_page.go_to_home_page()
        time.sleep(2)
        home_page.go_to_shopping_cart(driver)
        time.sleep(2)
        assert driver.current_url == "http://localhost/opencart/index.php?route=checkout/cart&language=en-gb"
    # navigate to wishlist
    def test_navigate_to_wishlist(self,driver):
        home_page = NavigationPage(driver)
        home_page.go_to_home_page()
        time.sleep(2)
        home_page.go_to_wishlist(driver)
        time.sleep(2)
        assert driver.current_url == "http://localhost/opencart/index.php?route=account/login&language=en-gb"

    # navigate to checkout
    def test_navigate_to_checkout(self,driver):
        home_page = NavigationPage(driver)
        home_page.go_to_home_page()
        time.sleep(2)
        home_page.go_to_checkout(driver)
        time.sleep(2)
        assert driver.current_url == "http://localhost/opencart/index.php?route=checkout/cart&language=en-gb"
    # navigate to product details
    def test_navigate_to_product_details(self,driver):
        home_page = NavigationPage(driver)
        home_page.go_to_home_page()
        time.sleep(2)
        home_page.go_to_product_details(driver)
        time.sleep(2)
        assert driver.current_url == "http://localhost/opencart/index.php?route=product/product&language=en-gb&product_id=43"
    # navigate to contactus
    def test_navigate_to_contactus(self,driver):
        home_page = NavigationPage(driver)
        home_page.go_to_home_page()
        time.sleep(2)
        home_page.go_to_contactus(driver)
        time.sleep(2)
        assert driver.current_url == "http://localhost/opencart/index.php?route=information/contact&language=en-gb"
