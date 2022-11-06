import re
import time

#from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN)

    def add_to_basket(self, prod_name, prod_price):
        self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BTN).click()
        self.solve_quiz_and_get_code()

        assert prod_name == self.browser.find_element(
            *ProductPageLocators.CONFIRMATION).text

    def check_sum_of_basket(self):
        WebDriverWait(self.browser, 3).until(EC.text_to_be_present_in_element_value(
            ProductPageLocators.MINI_BASKET, self.get_product_price()))
        assert self.get_product_name() == self.get_mini_basket_amount()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PROD_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PROD_PRICE).text

    def get_mini_basket_amount(self):
        el = self.browser.find_element(*ProductPageLocators.MINI_BASKET).text
        #print(el)
        return re.findall(r'\d+\,\d{2}', el)[0]
