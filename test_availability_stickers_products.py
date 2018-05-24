# Задания по тестированию LiteCart.
# Проверка наличия стикеров у всех товаров
# на главной странице сайта
# в учебном приложении LiteCart.

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class MasnerinOrder(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_orders_in_masnerin_com(self):
        driver = self.driver
        driver.get("http://localhost/litecart/en/")
        self.driver.maximize_window()
        self.assertIn("My LiteCart", driver.title)

        blocks = driver.find_elements_by_css_selector('a.link[data-toggle="lightbox"]') # Создание списка блоков товаров
        print("\nНайдено", len(blocks), "блоков.")

        for block in blocks:  # Цикл поиска наличия стикера в каждом блоке товара
            try:
                sticker = block.find_element_by_css_selector('div.sticker')
            except NoSuchElementException:
                print("В блоке:", block, "нет стикера!")
            print("В блоке:", block, "есть стикер.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
