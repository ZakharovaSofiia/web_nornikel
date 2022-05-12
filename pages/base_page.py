import allure
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def open(self):
        self.browser.get(self.url)

    def get_screenshot_error(self):
        allure.attach(
            name='Скриншот',
            body=self.browser.driver.get_screenshot_as_png(),
            attachment_type=allure.attachment_type.PNG
        )