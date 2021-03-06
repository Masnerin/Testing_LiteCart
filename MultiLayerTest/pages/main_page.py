from selenium.webdriver.support.wait import WebDriverWait


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get('http://localhost/litecart/en/')
        assert("My LiteCart", self.driver.title)
        return self

    def select_product(self):
        self.driver.find_element_by_css_selector('li.product').click()
