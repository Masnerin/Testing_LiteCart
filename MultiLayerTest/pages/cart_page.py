from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get('http://localhost/litecart/en/checkout')
        assert ("Checkout | My LiteCart", self.driver.title)
        return self

    def clean(self):
        products = self.driver.find_elements_by_css_selector('td.item')
        block = self.driver.find_element_by_css_selector('div#checkout-cart-wrapper')
        for i in range(len(products)):
            remove = self.driver.find_elements_by_css_selector('button[value = Remove]')
            for j in remove:
                self.wait.until(EC.visibility_of(block.find_element_by_css_selector('form[name=cart_form]')))
                self.wait.until(EC.visibility_of(j)).click()
                self.wait.until(EC.staleness_of(products[0]))
                break
            continue
        self.wait.until(EC.staleness_of(self.driver.find_element_by_css_selector('div#box-checkout-summary')))
        return self
