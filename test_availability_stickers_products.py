# Задания по тестированию LiteCart.
# Проверка наличия стикеров у всех товаров
# на главной странице сайта
# в учебном приложении LiteCart.

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class LabelsOnProducts(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_labels_on_products(self):
        driver = self.driver
        driver.get("http://localhost/litecart/en/")
        self.driver.maximize_window()
        self.assertIn("My LiteCart", driver.title)

        blocks = driver.find_elements_by_css_selector('div.image-wrapper')
        print("\nНайдено", len(blocks), "блоков товаров.")

        for block in blocks:
            sticker = block.find_elements_by_css_selector('div.sticker')
            if len(sticker) == 0: print("В блоке:", block, "нет стикера!")
            if len(sticker) == 1: print("В блоке:", block, "есть стикер.")
            if len(sticker) > 1: print("В блоке:", block, "более одного стикера!")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
