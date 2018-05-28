# Задания по тестированию LiteCart.
# Проверка открытия корректной страницы товара
# в учебном приложении litecart.


import re
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class CorrectProductPageTesting(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.wait = WebDriverWait(self.driver, 5)

    def test_correct_product_page(self):
        driver = self.driver
        driver.get("http://localhost/litecart")
        self.assertIn("My LiteCart", driver.title)

# Выбор товара
        product = driver.find_element_by_css_selector('div#box-campaigns')

# Проверка параметров товара на главной странице
        list_attr_prod = []  # Создание списка параметров товара на главной странице

        product_name = product.find_element_by_css_selector('div.name').get_attribute('textContent')
        list_attr_prod.append(product_name)
        print("\nНазвание продукта:", product_name)

        regular_price = product.find_element_by_css_selector('.regular-price').get_attribute('textContent')
        list_attr_prod.append(regular_price)

        regular_price_color = product.find_element_by_css_selector('.regular-price').value_of_css_property('color')
        list_attr_prod.append(regular_price_color)
        rpc = find_numbers(regular_price_color)
        if rpc[0] == rpc[1] == rpc[2]: print("Обычная цена серого цвета", end = ' ')
        else: print("Обычная цена не серого цвета", end = ' ')

        regular_price_stile = product.find_element_by_css_selector('.regular-price').value_of_css_property('text-decoration-line')
        list_attr_prod.append(regular_price_stile)
        st_regul = 'line-through'
        if regular_price_stile == st_regul: print("и зачёркнута.")
        else: print("и не зачёркнута.")

        campaign_price = product.find_element_by_css_selector('.campaign-price').get_attribute('textContent')
        list_attr_prod.append(campaign_price)

        campaign_price_color = product.find_element_by_css_selector('.campaign-price').value_of_css_property('color')
        list_attr_prod.append(campaign_price_color)
        cpc = find_numbers(campaign_price_color)
        if int(cpc[1]) == int(cpc[2]) == 0: print("Акционная цена красного цвета", end=' ')
        else: print("Акционная цена не красного цвета", end=' ')

        campaign_price_stile = product.find_element_by_css_selector('.campaign-price').get_attribute('localName')
        list_attr_prod.append(campaign_price_stile)
        st_camp = 'strong'
        if campaign_price_stile == st_camp: print("и жирная.")
        else: print("и не жирная.")

# Переход на страницу товара
        product_link = product.find_element_by_css_selector('a.link').get_attribute('href')
        driver.get(product_link)

# Извлечение параметров товара на странице товара
        list_attr_prod_b = []  # Создание списка параметров товара на странице товара
        product_b = driver.find_element_by_css_selector('div#box-product')
        product_name_b = product_b.find_element_by_css_selector('h1.title').get_attribute('textContent')
        list_attr_prod_b.append(product_name_b)
        regular_price_b = product_b.find_element_by_css_selector('.regular-price').get_attribute('textContent')
        list_attr_prod_b.append(regular_price_b)
        regular_price_color_b = product_b.find_element_by_css_selector('.regular-price').value_of_css_property('color')
        list_attr_prod_b.append(regular_price_color_b)
        regular_price_stile_b = product_b.find_element_by_css_selector('.regular-price').value_of_css_property('text-decoration-line')
        list_attr_prod_b.append(regular_price_stile_b)
        campaign_price_b = product_b.find_element_by_css_selector('.campaign-price').get_attribute('textContent')
        list_attr_prod_b.append(campaign_price_b)
        campaign_price_color_b = product_b.find_element_by_css_selector('.campaign-price').value_of_css_property('color')
        list_attr_prod_b.append(campaign_price_color_b)
        campaign_price_stile_b = product_b.find_element_by_css_selector('.campaign-price').get_attribute('localName')
        list_attr_prod_b.append(campaign_price_stile_b)

# Сравнение параметров товара на главной странице и на странице товара
        for i in range(0, len(list_attr_prod)):
            if list_attr_prod[i] == list_attr_prod_b[i]:
                print("Страница товара открывается корректно.")
                break
            print("!!! Некорректное открытие страницы товара !!!")

    def tear_down(self):
        self.driver.quit()

# Функция выделения чисел из строки
def find_numbers(string, ints=True):
    numexp = re.compile(r'[-]?\d[\d,]*[\.]?[\d{2}]*')  # optional - in front
    numbers = numexp.findall(string)
    numbers = [x.replace(',', '') for x in numbers]
    if ints is True:
        return [int(x.replace(',', '').split('.')[0]) for x in numbers]
    else:
        return numbers

if __name__ == "__main__":
        unittest.main()
