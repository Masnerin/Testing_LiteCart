# Задания по тестированию LiteCart.
# сценарий для добавления товаров в корзину
# и удаления товаров из корзины.
# в учебном приложении liteCart.


import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ProductsInTheCartTesting(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_products_in_the_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

# Вход на главную страницу
        driver.get("http://localhost/litecart")
        self.assertIn("My LiteCart", driver.title)

# Выбор товаров
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.link[title="Green Duck"]'))).click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[name="add_cart_product"]'))).click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'span.quantity'), '1'))
        driver.get("http://localhost/litecart")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.link[title="Red Duck"]'))).click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[name="add_cart_product"]'))).click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'span.quantity'), '2'))
        driver.get("http://localhost/litecart")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.link[title="Blue Duck"]'))).click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[name="add_cart_product"]'))).click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'span.quantity'), '3'))

# Удаление товаров из карзины
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.link'))).click()
        element = driver.find_element_by_css_selector('tr.footer')
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[value=Remove]'))).click()
        element = driver.find_element_by_css_selector('tr.footer')
        wait.until(EC.staleness_of(element))
        element = driver.find_element_by_css_selector('tr.footer')
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[value=Remove]'))).click()
        wait.until(EC.staleness_of(element))
        element = driver.find_element_by_css_selector('tr.footer')
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[value=Remove]'))).click()
        wait.until(EC.staleness_of(element))

        driver.get("http://localhost/litecart")

    def tear_down(self):
        driver.quit()

if __name__ == "__main__":
    unittest.main()
