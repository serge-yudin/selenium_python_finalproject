from selenium.common.exceptions import NoAlertPresentException

from .pages.product_page import ProductPage
import time

def is_there_add_to_basket_btn(self, browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.should_be_add_to_basket_btn()


def test_guest_can_add_product_to_basket(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'

    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.add_to_basket()
    
