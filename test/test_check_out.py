import time
from selenium.webdriver.edge import webdriver
from pages.home_page import NavigationPage
from pages.shoppingcart_page import ShoppingCartPage
from pages.login_page import LoginPage
from pages.check_out_page import CheckoutPage
from utils.webdriver_setup import Driver
from selenium.webdriver.common.by import By

class TestCheckout(Driver):
    def test_checkout_with_valid_info(self, driver):
        login_page = LoginPage(driver)
        email = "test@gmail.com"
        password = "test"
        login_page.go_to_login(email, password)
        time.sleep(3)

        # shoppingcart_page = ShoppingCartPage(driver)
        # shoppingcart_page.go_to_shopping_cart_page()
        # productname = "MacBook"
        # shoppingcart_page.search_product(productname)
        # shoppingcart_page.button_label_macbook()
        # time.sleep(3)
        # shoppingcart_page.button_label_air()
        # assert "Success: You have added" in shoppingcart_page.get_message()
        # time.sleep(3)

        checkout_page = CheckoutPage(driver)
        checkout_page.go_to_checkout_page()
        checkout_page.use_new_address()
        firstname = "test"
        lastname = "test"
        company = "TRANGIABAOGROUP"
        address1 = "82 Phan Huy Ich"
        address2 = "145/5 Phan Van Khoe"
        city = "Ho Chi Minh"
        postcode = "70000"
        checkout_page.input_feilds(firstname,lastname,company,address1, address2, city, postcode)
        checkout_page.shipping_method()
        checkout_page.payment_method()
        checkout_page.comfirm_order()
        assert "checkout/success" in driver.current_url
        time.sleep(3)

    def test_checkout_with_invalid_info(self,driver):
        login_page = LoginPage(driver)
        email = "test@gmail.com"
        password = "test"
        login_page.go_to_login(email, password)
        time.sleep(3)

        shoppingcart_page = ShoppingCartPage(driver)
        shoppingcart_page.go_to_shopping_cart_page()
        productname = "MacBook"
        shoppingcart_page.search_product(productname)
        shoppingcart_page.button_label_macbook()
        time.sleep(3)
        shoppingcart_page.button_label_air()
        assert "Success: You have added" in shoppingcart_page.get_message()
        time.sleep(3)

        checkout_page = CheckoutPage(driver)
        checkout_page.go_to_checkout_page()
        checkout_page.use_new_address()
        firstname = ""
        lastname = ""
        company = ""
        address1 = ""
        address2 = ""
        city = ""
        postcode = ""
        checkout_page.input_feilds(firstname, lastname, company, address1, address2, city, postcode)
        time.sleep(3)
        assert any("First Name must be between 1 and 32 characters!" in error for error in checkout_page.get_error_input())
        time.sleep(3)
