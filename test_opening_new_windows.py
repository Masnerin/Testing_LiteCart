# Задания по тестированию LiteCart.
# Сценарий проверки открытия новых окон
# в учебном приложении liteCart.


import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class OpeningNewWindowsTesting(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_opening_new_windows(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

# Вход в панель администрации:
        driver.get("http://localhost/litecart/admin")
        self.assertIn("My LiteCart", driver.title)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name=username]'))).send_keys("admin")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name=password]'))).send_keys("admin")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[name=login]'))).click()
        self.assertIn("My LiteCart", driver.title)

# Вход на страницу создания страны:
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Countries"]'))).click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.button'))).click()

# Поиск ссылок и проверка открытия новых окон:
        main_window = driver.current_window_handle
        old_windows = driver.window_handles
        links = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'i.fa.fa-external-link')))
        for i in range(0, len(links)):
            str_links = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'i.fa.fa-external-link')))
            str_links[i].click()
            wait.until(EC.new_window_is_opened(old_windows))
            new_windows = driver.window_handles
            result = list(set(new_windows) - set(old_windows))
            new_window = result[0]
            driver.switch_to.window(new_window)
            driver.close()
            driver.switch_to.window(main_window)

    def tear_down(self):
        driver.quit()

if __name__ == "__main__":
    unittest.main()
