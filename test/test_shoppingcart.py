import time
from selenium.webdriver.edge import webdriver
from pages.shoppingcart_page import ShoppingCartPage
from pages.home_page import NavigationPage
from utils.webdriver_setup import Driver
from selenium.webdriver.common.by import By


class TestShoppingCart(Driver):
    # add product to cart
    def test_add_product_to_cart(self, driver):
        shopping_cart_page = ShoppingCartPage(driver)
        shopping_cart_page.go_to_shopping_cart_page()
        shopping_cart_page.add_product_to_cart_macbook()
        assert "Success: You have added" in shopping_cart_page.get_message()
        time.sleep(3)

    # add product with quantity
    def test_add_product_with_quantity(self, driver):
        shopping_cart_page = ShoppingCartPage(driver)
        shopping_cart_page.details_product_macbook()
        shopping_cart_page.quantity(2)
        shopping_cart_page.add_more_product()
        assert "Success: You have added" in shopping_cart_page.get_message()
        time.sleep(3)

    # add product with zero quantity
    def test_add_product_zero_quantity(self, driver):
        shopping_cart_page = ShoppingCartPage(driver)
        shopping_cart_page.details_product_macbook()
        shopping_cart_page.quantity(0)
        shopping_cart_page.add_more_product()
        assert "Success: You have added" in shopping_cart_page.get_message()
        time.sleep(3)
     # loi van hien thi them duoc san pham khi nhap 0

    # add product with negative quantity
    def test_add_product_negative_quantity(self, driver):
        shopping_cart_page = ShoppingCartPage(driver)
        shopping_cart_page.details_product_macbook()
        shopping_cart_page.quantity(-1)
        shopping_cart_page.add_more_product()
        assert "Success: You have added" in shopping_cart_page.get_message()
        time.sleep(3)
    # loi van hien thi them duoc san pham khi nhap -1

    # add product without quantity
    def test_add_product_without_quantity(self, driver):
        shopping_cart_page = ShoppingCartPage(driver)
        shopping_cart_page.details_product_macbook()
        shopping_cart_page.clear_quantity()
        shopping_cart_page.add_more_product()
        assert "Success: You have added" in shopping_cart_page.get_message()
        time.sleep(3)
    # loi van hien thi them duoc san pham khi nhap rong

    # remove product
    def test_remove_product(self, driver):
        shopping_cart_page = ShoppingCartPage(driver)
        self.test_add_product_to_cart(driver)
        shopping_cart_page.go_to_shopping_cart_page()
        shopping_cart_page.remove_product()
        assert driver.page_source.find("/html/body/main/div[2]/div/div/h1") != 0
        time.sleep(3)

    # update product
    def test_update_product(self, driver):
        shopping_cart_page = ShoppingCartPage(driver)
        self.test_add_product_to_cart(driver)
        shopping_cart_page.go_to_shopping_cart_page()
        shopping_cart_page.update_product()
        assert "Success: You have modified your shopping cart!" in shopping_cart_page.get_message()
        time.sleep(3)

    # add multiple product
    def test_add_multiple_product(self, driver):
        shopping_cart_page = ShoppingCartPage(driver)
        shopping_cart_page.go_to_shopping_cart_page()
        productname = "MacBook"
        shopping_cart_page.search_product(productname)
        shopping_cart_page.button_label_macbook()
        time.sleep(3)
        shopping_cart_page.button_label_air()
        assert "Success: You have added" in shopping_cart_page.get_message()
        time.sleep(3)