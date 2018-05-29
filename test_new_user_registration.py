# Задания по тестированию LiteCart.
# Проверка регистрации нового пользователя
# в учебном приложении liteCart.


import time
import random
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


class NewUserRegistrationTesting(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.wait = WebDriverWait(self.driver, 5)

    def test_new_user_registration(self):
        driver = self.driver
        driver.get("http://localhost/litecart")
        self.assertIn("My LiteCart", driver.title)

# Регистрация нового пользователя
        driver.find_element_by_css_selector('form[name=login_form] a').click()
        FirstName = GenUserName()
        driver.find_element_by_css_selector('input[name=firstname]').send_keys(FirstName)
        LastName = GenUserName()
        driver.find_element_by_css_selector('input[name=lastname]').send_keys(LastName)
        driver.find_element_by_css_selector('input[name=address1]').send_keys('Kosti Palama, 27')
        driver.find_element_by_css_selector('input[name=postcode]').send_keys('64100')
        driver.find_element_by_css_selector('input[name=city]').send_keys('Chalkis')
        Select(driver.find_element_by_css_selector('select[name=country_code]')).select_by_value('US')
        Email = GenMail()
        driver.find_element_by_css_selector('input[name=email]').send_keys(Email)
        driver.find_element_by_css_selector('input[name=phone]').send_keys('6907734234')
        driver.find_element_by_css_selector('input[name=password]').send_keys('password')
        driver.find_element_by_css_selector('input[name=confirmed_password]').send_keys('password')
        driver.find_element_by_css_selector('button[name=create_account]').click()

# Выход из аккаунта
        driver.find_element_by_link_text("Logout").click()

# Вход в аккаунт по зарегистрированным данным
        driver.find_element_by_css_selector('input[name=email]').send_keys(Email)
        driver.find_element_by_css_selector('input[name=password]').send_keys('password')
        time.sleep(5)
        driver.find_element_by_css_selector('button[name=login]').click()

# Окончательный выход из аккаунта
        driver.find_element_by_link_text("Logout").click()

# Функция создания уникального e-mail
def GenMail():
    array = [chr(i) for i in range(65, 91)]
    random.shuffle(array)
    key = ""
    for i in range(7):
        key += array.pop()
    mail = key.lower() + '@randmail.com'
    return mail

# Функция создания уникального имени пользователя
def GenUserName():
    array = [chr(i) for i in range(65, 91)]
    random.shuffle(array)
    key = ""
    for i in range(7):
        key += array.pop()
    user_name = key.title()
    return user_name

if __name__ == "__main__":
        unittest.main()
