import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--city', action='store', default='monchegorsk', help='Choose city: dudinka, monchegorsk...')


@pytest.fixture()
def get_city(request):
    city = request.config.getoption('city')
    return city


@pytest.fixture()
def browser(request):
    options = Options()
    browser = webdriver.Chrome(options=options)
    yield browser
    print("quit browser")
    browser.quit()
