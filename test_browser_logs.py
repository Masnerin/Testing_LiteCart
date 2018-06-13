# Задания по тестированию LiteCart.
# Проверка появления сообщений в логе браузера
# при открытии страниц в каталоге товаров
# в панеле администрации учебного приложения LiteCart.

import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BrowserLogsTesting(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_browser_logs(self):
        driver = self.driver
        driver.wait = WebDriverWait(driver, 10)
        driver.get("http://localhost/litecart/admin")
        self.assertIn("My LiteCart", driver.title)

# Вход в панель администрации:
        try:
            driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name=username]'))).send_keys(
                "admin")
            driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name=password]'))).send_keys(
                "admin")
            driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[name=login]'))).click()
        except TimeoutException: print("Box or Button not found!")
        self.assertIn("My LiteCart", driver.title)


# Открытие страницы категории с товарами:
        driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Catalog']"))).click()
        driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Rubber Ducks']"))).click()
        number_products = driver.wait.until(EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, "Duck")))
        for i in range(1, len(number_products)):
            products = driver.wait.until(EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, "Duck")))
            products[i].click()
            product_name = driver.find_element_by_css_selector('input[name="name[en]"]').get_attribute('value')
            print(i, '-', product_name)
            for log in driver.get_log("browser"):
                print("Message:", log)
            driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Catalog']"))).click()
            driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Rubber Ducks']"))).click()

    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
