import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)
        self._login_button = (By.CSS_SELECTOR, '[data-testid="loginButton"]')

    @allure.step('Переходим на страницу логина')
    def go_to_login_page(self):
        self.browser.find_element(*self._login_button).click()
        from pages.login_page import LoginPage
        return LoginPage(browser=self.browser, url=self.browser.current_url)
