from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.quantity = 0
        self.wait = WebDriverWait(driver, 10)

    def select_product_size(self):
        size = self.driver.find_elements_by_css_selector('select')
        if len(size) != 0:
            Select(self.driver.find_element_by_css_selector('select')).select_by_index(1)

    def product_in_cart(self):
        self.quantity += 1
        self.driver.find_element_by_css_selector('button[name="add_cart_product"]').click()
        self.wait.until(lambda d: d.find_element_by_xpath('//span[starts-with(text(), {})]'.format(str(self.quantity))))
        return self

