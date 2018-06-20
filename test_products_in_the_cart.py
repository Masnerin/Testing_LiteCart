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
        products = self.driver.find_elements_by_css_selector('td.item')
        block = self.driver.find_element_by_css_selector('div#checkout-cart-wrapper')
        for i in range(len(products)):
            remove = self.driver.find_elements_by_css_selector('button[value = Remove]')
            for j in remove:
                driver.wait.until(EC.visibility_of(block.find_element_by_css_selector('form[name=cart_form]')))
                driver.wait.until(EC.visibility_of(j)).click()
                driver.wait.until(EC.staleness_of(products[0]))
                break
            continue
        driver.wait.until(EC.staleness_of(self.driver.find_element_by_css_selector('div#box-checkout-summary')))
        return self

    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
