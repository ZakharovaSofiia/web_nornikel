from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Не отображается форма регистрации'

    def should_be_recaptcha_form(self):
        assert self.is_element_present(*LoginPageLocators.RECAPTCHA_FORM), 'Не отображается captcha регистрации'

    def should_be_confirm_registration_form(self):
        assert self.is_element_present(*LoginPageLocators.CONFIRM_REGISTRATION_CODE), 'Не отображается окно подтверждения регистрации'
