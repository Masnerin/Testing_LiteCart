# Задания по тестированию LiteCart.
# Локальный хост AMPPS на Windows10.
# Тестирование входа в админку.

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class LitecartAdminLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('C:\\Masnerin\\WebDriver\\Chrome\\chromedriver.exe')

    def test_orders_in_masnerin_com(self):
        driver = self.driver
        driver.get("http://localhost/litecart/admin/login.php")
        self.driver.maximize_window()
        self.assertIn("My LiteCart", driver.title)

        elem = driver.find_element_by_name("username")
        elem.send_keys("admin")

        elem = driver.find_element_by_name("password")
        elem.send_keys("admin")

        button = driver.find_element_by_xpath("//*[text()='Login']")
        button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
