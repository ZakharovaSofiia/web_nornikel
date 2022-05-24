import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    def _scroll_to(self, how, what):
        element = self.browser.find_element(how, what)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)

    def wait_element_to_be_clickable(self, how, what):
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((how, what)))