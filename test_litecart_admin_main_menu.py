# Задания по тестированию LiteCart
# Тестирование элементов главного меню админки

import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LitecartAdminMainMenuTesting(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.wait = WebDriverWait(self.driver, 10)

    def test_litecart_admin_main_menu(self):
        driver = self.driver
        driver.get("http://localhost/litecart/admin")
        self.assertIn("My LiteCart", driver.title)

        try:
            box_usern = driver.wait.until(EC.presence_of_element_located((By.NAME, "username")))
            box_usern.send_keys("admin")
            box_passw = driver.wait.until(EC.presence_of_element_located((By.NAME, "password")))
            box_passw.send_keys("admin")
            button = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Login']")))
            button.click()
        except TimeoutException:
            print("Box or Button not found!")
        self.assertIn("My LiteCart", driver.title)

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Appearance']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Template']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Logotype']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Catalog']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Product Groups']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Option Groups']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Manufacturers']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Suppliers']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Delivery Statuses']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Sold Out Statuses']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Quantity Units']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='CSV Import/Export']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Countries']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Currencies']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Customers']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='CSV Import/Export']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Newsletter']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Geo Zones']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Languages']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Storage Encoding']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Modules']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Customer Modules']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Shipping Modules']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Payment Modules']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Order Modules']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Order Total Modules']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Job Modules']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Orders']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Order Statuses']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Pages']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='CSV Import/Export']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Reports']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Monthly Sales']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Most Sold Products']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Most Shopping Customers']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Settings']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Store Info']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Defaults']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Email']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Listings']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Images']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Checkout']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Advanced']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Security']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Slides']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Tax']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Tax Rates']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Tax Classes']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Translations']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Search Translations']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Scan Files']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='CSV Import/Export']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Users']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='vQmods']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        except NoSuchElementException:
            print('"h1" tag not found')

        try:
            elem_menu = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@class ='center-block img-responsive']")))
            elem_menu.click()
        except TimeoutException:
            print("Element of menu not found!")
        self.assertIn("My LiteCart", driver.title)


    def tear_down(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()