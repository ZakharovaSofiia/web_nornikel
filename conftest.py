import os

import allure
import pytest
from pages.base_page import BasePage
from selenium import webdriver


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
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--start-maximized')
        print('start Chrome browser for test...')
        browser = webdriver.Chrome(options=chrome_options)
        browser.implicitly_wait(3)
    elif browser_name == 'firefox':
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--start-maximized')
        print('start Firefox browser for test...')
        browser = webdriver.Firefox(options=firefox_options)
        browser.implicitly_wait(3)
    yield browser
    print("quit browser")
    browser.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'browser' in item.fixturenames:
                    web_driver = item.funcargs['browser']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))