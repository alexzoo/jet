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

    url = 'http://yandex.ru'
    driver = webdriver.Chrome('./chromedriver')
    driver.wait = WebDriverWait(driver, 5)

    def lookup(self, query):
        self.driver.get(self.url)
        search_field = self.driver.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@id='text']")))
        search_field.send_keys(query)
        search_res = self.driver.wait.until(EC.visibility_of_element_located((By.XPATH, "//li[1]//span[1]//b[1]")))
        print()

    def test_yandex(self):
        self.lookup('погода')

        self.driver.quit()



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

    #     button = self.driver.wait.until(EC.element_to_be_clickable(
    #         (By.NAME, "btnK")))
    #     box.send_keys(query)
    #
    #     try:
    #         button.click()
    #     except ElementNotVisibleException:
    #         button = driver.wait.until(EC.visibility_of_element_located(
    #             (By.NAME, "btnG")))
    #         button.click()
    #
    #
    # except TimeoutException:
    # print("Box or Button not found in google.com")
