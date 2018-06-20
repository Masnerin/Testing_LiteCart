# Задания по тестированию LiteCart.
# сценарий для добавления товаров в корзину
# и удаления товаров из корзины.
# в учебном приложении liteCart.


import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select


class ProductsInTheCartTesting(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_products_in_the_cart(self):
        driver = self.driver
        driver.wait = WebDriverWait(driver, 10)

# Вход на главную страницу
        driver.get("http://localhost/litecart")
        self.assertIn("My LiteCart", driver.title)

# Выбор товаров
        for j in range(1, 4):
            driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li.product'))).click()
            size = driver.find_elements_by_css_selector('select')
            if len(size) != 0:
                Select(driver.find_element_by_css_selector('select')).select_by_index(1)
            driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[name="add_cart_product"]'))).click()
            driver.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'span.quantity'), str(j)))

# Удаление товаров из корзины
        driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.link'))).click()
        number_product = driver.find_elements_by_css_selector('li.shortcut')
        for i in range(0, len(number_product)):
            element = driver.find_elements_by_css_selector('table.dataTable.rounded-corners tr')
            a = len(element)
            driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[value=Remove]'))).click()
            driver.wait.until(EC.staleness_of(element[a - 1]))

    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
