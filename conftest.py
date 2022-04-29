import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--city', action='store', default='monchegorsk', help='Choose city: dudinka, monchegorsk...')
    parser.addoption('--browser_name', action='store', default='chrome', help='Choose browser: chrome or firefox...')


@pytest.fixture()
def get_city(request):
    city = request.config.getoption('city')
    return city


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption('browser_name')
    browser = None
    if browser_name == 'chrome':
        print('start Chrome browser for test...')
        browser = webdriver.Chrome()
        browser.implicitly_wait(3)
    elif browser_name == 'firefox':
        print('start Firefox browser for test...')
        browser = webdriver.Firefox()
        browser.implicitly_wait(3)
    yield browser
    print("quit browser")
    browser.quit()
