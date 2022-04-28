from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_link.click()
