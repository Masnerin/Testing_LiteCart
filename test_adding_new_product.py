# Задания по тестированию LiteCart.
# Проверка добавления нового товара
# в учебном приложении liteCart.


import os
import random
import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select


class AddingNewProductTesting(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.wait = WebDriverWait(self.driver, 10)

    def test_adding_new_product(self):
        driver = self.driver
        driver.get("http://localhost/litecart/admin")
        self.assertIn("My LiteCart", driver.title)

# Вход в административную панель
        try:
            driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name=username]'))).send_keys(
                "admin")
            driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name=password]'))).send_keys(
                "admin")
            driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[name=login]'))).click()
        except TimeoutException:
            print("Box or Button not found!")
        self.assertIn("My LiteCart", driver.title)

# Вход в раздел добавления товара
        driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'ul#box-apps-menu li:nth-child(2)'))).click()
        driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'td#content a.button:nth-child(2)'))).click()

# Заполнение раздела "General"
        driver.find_element_by_css_selector('input[name=status]').click()
        driver.find_element_by_css_selector('input[name="name[en]"]').send_keys('New product')
        code_product = RandomKod()
        driver.find_element_by_css_selector('input[name="code"]').send_keys(code_product)
        prod_grups = driver.find_elements_by_css_selector('input[name="product_groups[]"]')
        prod_grups[2].click()
        quantity = driver.find_element_by_css_selector('input[name=quantity]')
        quantity.clear()
        quantity.send_keys(10)
        driver.find_element_by_css_selector('select[name=sold_out_status_id] option[value="2"]').click()
        driver.find_element_by_css_selector('input[type=file]').send_keys(os.getcwd() + "\product_new.jpg")
        driver.find_element_by_css_selector('input[name=date_valid_from]').send_keys('30052018')
        driver.find_element_by_css_selector('input[name=date_valid_to]').send_keys('31122018')

# Заполнение раздела "Information"
        a = driver.find_elements_by_css_selector('ul.index a')
        a[1].click()

        Select(driver.find_element_by_css_selector('select[name=manufacturer_id]')).select_by_index(1)
        driver.find_element_by_css_selector('input[name=keywords]').send_keys("product, new product")
        driver.find_element_by_css_selector('input[name="short_description[en]"]').send_keys("New product for sale")
        driver.find_element_by_css_selector('div.trumbowyg-editor').send_keys(
        "Why do we use it?\nGirl quit if case mr sing as no have. Small for ask shade water manor think men begin."
                                                                              )
        driver.find_element_by_css_selector('input[name="head_title[en]"]').send_keys("New product")
        driver.find_element_by_css_selector('input[name="meta_description[en]"]').send_keys("Very good product.")

# Заполнение раздела "Prices"
        a = driver.find_elements_by_css_selector('ul.index a')
        a[3].click()

        price = driver.find_element_by_css_selector('input[name=purchase_price]')
        price.clear()
        price.send_keys('19,99')
        driver.find_element_by_css_selector('select option[value=EUR]').click()
        tax = driver.find_element_by_css_selector('input[name="prices[USD]"]')
        tax.clear()
        tax.send_keys('34,99')
        tax = driver.find_element_by_css_selector('input[name="prices[EUR]"]')
        tax.clear()
        tax.send_keys('29,99')
        driver.find_element_by_css_selector('button[name=save]').click()

    def tear_down(self):
        self.driver.quit()

# Функция создания кода товара
def RandomKod():
    kod = ''
    for x in range(32):
        kod = kod + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwz'))
    return kod

if __name__ == "__main__":
    unittest.main()
