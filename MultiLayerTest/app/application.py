from selenium import webdriver
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.main_page = MainPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.cart_page = CartPage(self.driver)

    def quit(self):
        self.driver.quit()

    def product_selection(self):
        self.main_page.open()
        self.main_page.select_product()

    def product_in_cart(self):
        self.product_page.select_product_size()
        self.product_page.product_in_cart()

    def clean_the_cart(self):
        self.cart_page.open()
        self.cart_page.clean()
