# Задания по тестированию LiteCart.
# Проверка сортировки стран и геозон (штатов)
# в панеле администрации учебного приложения litecart.

import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ListCountriesSortingTesting(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.wait = WebDriverWait(self.driver, 5)

    def test_litecart_sorting_countres_zones(self):
        driver = self.driver
        driver.get("http://localhost/litecart/admin")
        self.assertIn("My LiteCart", driver.title)

# Вход в панель администрации:
        try:
            driver.wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("admin")
            driver.wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("admin")
            driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Login']"))).click()
        except TimeoutException:
            print("Box or Button not found!")
        self.assertIn("My LiteCart", driver.title)

        print("\nЗадание 9.")

# Открытие страницы 'Countries':
        driver.wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()='Countries']"))).click()
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1')))
        except NoSuchElementException:
            print('"h1" tag not found')

# Проверка сортировки списка стран:
        trs = driver.find_elements_by_css_selector('tbody tr')
        countries = []
        countries_sort = []
        for i in range(0, len(trs)):
            tds = trs[i].find_elements_by_css_selector('td')
            countrie = tds[4].get_attribute('textContent')
            countries.append(countrie)
            countries_sort.append(countrie)
        print("\n1. Количество стран на странице 'Countries':", len(countries))
        countries_sort.sort()
        for j in range(0, len(countries)):
            if countries[j] != countries_sort[j]:
                print("= Список стран не сортирован!")
                break
        print("= Список стран сортирован.")

# Нахождение стран, имеющих зоны (штаты):
        trs = driver.find_elements_by_css_selector('tbody tr')
        for n in range(0, len(trs)):
            tds = trs[n].find_element_by_css_selector('td.text-center')
            number_zones = tds.get_attribute('textContent')
            if int(number_zones) == 0:
                continue
            print("В стране", countries[n], "есть зоны.")
            tds = trs[n].find_element_by_css_selector('a').click()

            trs_z = driver.find_elements_by_css_selector('tbody tr')
            zones = []
            zones_sort = []
            for i in range(0, len(trs_z)):
                tds_z = trs_z[i].find_elements_by_css_selector('td')
                zone = tds_z[3].get_attribute('textContent')
                zones.append(zone)
                zones_sort.append(zone)
            print("Количество найденных зон:", len(zones))
            zones_sort.sort()
            for j in range(0, len(zones)):
                if zones[j] != zones_sort[j]:
                    print("= Список зон не сортирован!")
                    break
            print("= Список зон сортирован.")
            driver.find_element_by_xpath("//*[text()='Countries']").click()
            trs = driver.find_elements_by_css_selector('tbody tr')

# Отркрытие страницы 'Geo Zones'
        driver.wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()='Geo Zones']"))).click()
        try:
            elem_page = driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1')))
        except NoSuchElementException:
            print('"h1" tag not found')

# Проверка сортировки списка геозон:
        trs = driver.find_elements_by_css_selector('tbody tr')
        countries = []
        countries_sort = []
        for i in range(0, len(trs)):
            tds = trs[i].find_elements_by_css_selector('td')
            countrie = tds[2].get_attribute('textContent')
            countries.append(countrie)
            countries_sort.append(countrie)
        print("\n2. Количество геозон на странице 'Geo Zones':", len(countries))
        countries_sort.sort()
        for j in range(0, len(countries)):
            if countries[j] != countries_sort[j]:
                print("= Список геозон не сортирован!")
                break
        print("= Список геозон сортирован.")

# Нахождение геозон, имеющих зоны:
        trs = driver.find_elements_by_css_selector('tbody tr')
        for n in range(0, len(trs)):
            tds = trs[n].find_element_by_css_selector('td.text-center')
            number_zones = tds.get_attribute('textContent')
            if int(number_zones) == 0:
                continue
            print("В геозоне", countries[n], "есть зоны.")
            tds = trs[n].find_element_by_css_selector('a').click()

            trs_z = driver.find_elements_by_css_selector('tbody tr')
            zones = []
            zones_sort = []
            for i in range(0, len(trs_z)):
                tds_z = trs_z[i].find_elements_by_css_selector('td')
                zone = tds_z[1].get_attribute('textContent')
                zones.append(zone)
                zones_sort.append(zone)
            print("Количество найденных зон:", len(zones))
            zones_sort.sort()
            for j in range(0, len(zones)):
                if zones[j] != zones_sort[j]:
                    print("= Список зон не сортирован!")
                    break
            print("= Список зон сортирован.")
            driver.find_element_by_xpath("//*[text()='Geo Zones']").click()
            trs = driver.find_elements_by_css_selector('tbody tr')

    def tear_down(self):
        self.driver.quit()

if __name__ == "__main__":
        unittest.main()
