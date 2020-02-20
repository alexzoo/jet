from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestYandex:

    url = 'http://yandex.ru'
    driver = webdriver.Chrome('./chromedriver')
    driver.wait = WebDriverWait(driver, 5)

    def lookup(self, words):
        result = []
        self.driver.get(self.url)

        for word in words:
            res = self.search(word)
            result.append(res)
        return result

    def search(self, query):
        search_field = self.driver.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@id='text']")))
        search_field.clear()
        search_field.send_keys(query)
        search_res = self.driver.wait.until(EC.visibility_of_element_located((By.XPATH, "//li[1]//span[1]//b[1]")))
        search_text = search_res.get_attribute('innerHTML')
        return search_text

    def test_yandex(self):
        words = ['погода', 'Липецк', 'Лото']

        res = self.lookup(words)
        print('*********************')
        print(res)
        self.driver.quit()

