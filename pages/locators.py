from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#registration_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, 'form#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, 'form#register_form')


class ProductPageLocators:
    PROD_NAME = (By.CSS_SELECTOR, 'article h1')
    PROD_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    CONFIRMATION = (By.CSS_SELECTOR, '#messages .alert-success strong')
    MINI_BASKET = (By.CSS_SELECTOR, 'div.basket-mini')
