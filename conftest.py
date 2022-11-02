import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                    help='Set your desired language for UI')


@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption('language')
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


