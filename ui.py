import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException


class TestYandex:

    def init_driver(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.wait = WebDriverWait(self.driver, 5)
        return self.driver

    def lookup(self, driver, url, query):
        driver.get(url)
        try:
            box = driver.wait.until(EC.presence_of_element_located(
                (By.NAME, "q")))
            button = driver.wait.until(EC.element_to_be_clickable(
                (By.NAME, "btnK")))
            box.send_keys(query)
            try:
                button.click()
            except ElementNotVisibleException:
                button = driver.wait.until(EC.visibility_of_element_located(
                    (By.NAME, "btnG")))
                button.click()
        except TimeoutException:
            print("Box or Button not found in google.com")

    def test_yandex(self):

        driver = self.init_driver()
        self.lookup(driver, 'http://yandex.ru', 'погода')


        # driver.get("http://yandex.ru")
        # search_field = driver.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='text']")))
        # search_field.send_keys("погода")
        # search_field.submit()
        #
        # # try:
        # #     search_field = driver.wait.until(EC.element_to_be_clickable(By.XPATH, "//input[@id='text']"))
        # #     search_field.send_keys('погода')
        # # except TimeoutException:
        # #     print("Box or Button not found in google.com")
        driver.quit()





