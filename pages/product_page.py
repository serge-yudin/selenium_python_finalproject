from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN)

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN).click()
        self.solve_quiz_and_get_code()
        prod_name = self.browser.find_element(*ProductPageLocators.PROD_NAME).text
        assert prod_name in self.browser.find_element(*ProductPageLocators.CONFIRMATION).text

