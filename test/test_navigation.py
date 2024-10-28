import time

from pages.home_page import NavigationPage
from utils.webdriver_setup import Driver
from selenium.webdriver.common.by import By

class TestNavigation(Driver):
    def test_navigate_to_desktop(self,driver):
        home_page = NavigationPage(driver)
        home_page.go_to_home_page()
        time.sleep(2)
        home_page.go_to_all_desktops(driver)
        time.sleep(2)
        assert driver.current_url == "http://localhost/opencart/index.php?route=product/category&language=en-gb&path=20"

    def test_navigate_to_laptop(self,driver):
        home_page = NavigationPage(driver)
        home_page.go_to_home_page()
        time.sleep(2)
        home_page.go_to_all_laptops(driver)
        time.sleep(2)
        assert driver.current_url == "http://localhost/opencart/index.php?route=product/category&language=en-gb&path=18"

    def test_navigate_to_component(self,driver):
        home_page = NavigationPage(driver)
        home_page.go_to_home_page()
        time.sleep(2)
        home_page.go_to_all_components(driver)
        time.sleep(2)
        assert driver.current_url == "http://localhost/opencart/index.php?route=product/category&language=en-gb&path=25"

    def test_navigate_to_tablet(self,driver):
        home_page = NavigationPage(driver)
        home_page.go_to_home_page()
        time.sleep(2)
        home_page.go_to_tablet(driver)
        time.sleep(2)
        assert driver.current_url == "http://localhost/opencart/index.php?route=product/category&language=en-gb&path=57"

    def test_navigate_to_software(self,driver):
        home_page = NavigationPage(driver)
        home_page.go_to_home_page()
        time.sleep(2)
        home_page.go_to_software(driver)
        time.sleep(2)
        assert driver.current_url == "http://localhost/opencart/index.php?route=product/category&language=en-gb&path=17"


    def test_navigate_to_phones(self,driver):
        home_page = NavigationPage(driver)
        home_page.go_to_home_page()
        time.sleep(2)
        home_page.go_to_phones(driver)
        time.sleep(2)
        assert driver.current_url == "http://localhost/opencart/index.php?route=product/category&language=en-gb&path=19"

    def test_navigate_to_cameras(self,driver):
        home_page = NavigationPage(driver)
        home_page.go_to_home_page()
        time.sleep(2)
        home_page.go_to_cameras(driver)
        time.sleep(2)
        assert driver.current_url == "http://localhost/opencart/index.php?route=product/category&language=en-gb&path=33"

    def test_navigate_to_shopping_cart(self,driver):
        home_page = NavigationPage(driver)
        home_page.go_to_home_page()
        time.sleep(2)
        home_page.go_to_shopping_cart(driver)
        time.sleep(2)
        assert driver.current_url == "http://localhost/opencart/index.php?route=checkout/cart&language=en-gb"

    def test_navigate_to_wishlist(self,driver):
        home_page = NavigationPage(driver)
        home_page.go_to_home_page()
        time.sleep(2)
        home_page.go_to_wishlist(driver)
        time.sleep(2)
        assert driver.current_url == "http://localhost/opencart/index.php?route=account/login&language=en-gb"

    def test_navigate_to_checkout(self,driver):
        home_page = NavigationPage(driver)
        home_page.go_to_home_page()
        time.sleep(2)
        home_page.go_to_checkout(driver)
        time.sleep(2)
        assert driver.current_url == "http://localhost/opencart/index.php?route=checkout/cart&language=en-gb"

    def test_navigate_to_product_details(self,driver):
        home_page = NavigationPage(driver)
        home_page.go_to_home_page()
        time.sleep(2)
        home_page.go_to_product_details(driver)
        time.sleep(2)
        assert driver.current_url == "http://localhost/opencart/index.php?route=product/product&language=en-gb&product_id=43"

    def test_navigate_to_contactus(self,driver):
        home_page = NavigationPage(driver)
        home_page.go_to_home_page()
        time.sleep(2)
        home_page.go_to_contactus(driver)
        time.sleep(2)
        assert driver.current_url == "http://localhost/opencart/index.php?route=information/contact&language=en-gb"