import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)
        self._register_form = (By.CSS_SELECTOR, '#credential-modal-form')
        self._registration_by_email = (By.CSS_SELECTOR, '[data-testid="credential-by-email"]')
        self._email_input = (By.CSS_SELECTOR, '[data-testid="registration-by-email-input"]')
        self._email_password_input = (By.CSS_SELECTOR, '[data-testid="registration-by-email-password-input"]')
        self._confirm_email_password_input = (By.CSS_SELECTOR, '[data-testid="registration-by-email-confirm-password-input"]')
        self._registration_agreement = (By.XPATH, '//*[@data-testid="registration-agreement-input"]/..//*[@fill="none"]')
        self._registration_button = (By.CSS_SELECTOR, '[data-testid="registration-button"]')
        self._recaptcha_form = (By.CSS_SELECTOR, '#recaptcha-token')
        self._confirm_registration_code = (By.CSS_SELECTOR, '[data-testid = "code-confirmation-prompt"]')

    @allure.step('Регистрация пользователя')
    def registration_user(self, email, password):
        self.browser.find_element(*self._registration_by_email).click()
        self.browser.find_element(*self._email_input).send_keys(email)
        self.browser.find_element(*self._email_password_input).send_keys(password)
        self._scroll_to(*self._confirm_email_password_input)
        self.browser.find_element(*self._confirm_email_password_input).send_keys(password)
        self.browser.find_element(*self._registration_agreement).click()
        self.browser.find_element(*self._registration_button).click()

    @allure.step('Проверяем отображение формы регистрации')
    def should_be_register_form(self):
        assert self.is_element_present(*self._register_form), 'Не отображается форма регистрации'

    @allure.step('Проверяем отображение подтверждения регистрации и captcha')
    def should_be_confirm_registration_form(self):
        assert any((self.is_element_present(*self._confirm_registration_code),
                    self.is_element_present(*self._recaptcha_form))), 'Не отображается окно подтверждения регистрации/captcha'

