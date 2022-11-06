import pytest

from .pages.product_page import ProductPage


@pytest.mark.skip()
def test_is_there_add_to_basket_btn(browser):
    # 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.should_be_add_to_basket_btn()

@pytest.mark.parametrize('offer', tuple(range(10)))
def test_guest_can_add_product_to_basket(browser, offer):
    # 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    url = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer}'
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.add_to_basket(
        product_page.get_product_name(), product_page.get_product_price())


@pytest.mark.skip()
def test_should_be_product_price_in_basket(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.check_sum_of_basket()
