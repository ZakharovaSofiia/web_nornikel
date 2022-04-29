from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-testid="login-header-button"]')
    REGISTER_FORM = (By.CSS_SELECTOR, '#credential-modal-form')
