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


        items_apps = driver.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li#app-')))

        for i in range(0, len(items_apps)):
            items = driver.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li#app-')))
            items[i].click()
            try:
                elem_page = driver.wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
            except NoSuchElementException:
                print('"h1" tag not found')

            try:
                docs = driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul.docs')))
            except NoSuchElementException:
                print("Нет вложенных пунктов!")
                continue

            items_docs = driver.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'ul.docs a')))
            for j in range(0, len(items_docs)):
                item_doc = driver.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'ul.docs a')))
                item_doc[j].click()
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
