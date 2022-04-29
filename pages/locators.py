from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-testid="login-header-button"]')
    REGISTER_FORM = (By.CSS_SELECTOR, '#credential-modal-form')
    REGISTRATION_BY_EMAIL = (By.CSS_SELECTOR, '[data-testid="credential-by-email"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, '[data-testid="registration-by-email-input"]')
    EMAIL_PASSWORD_INPUT = (By.CSS_SELECTOR, '[data-testid="registration-by-email-password-input"]')
    CONFIRM_EMAIL_PASSWORD_INPUT = (By.CSS_SELECTOR, '[data-testid="registration-by-email-confirm-password-input"]')
    REGISTRATION_AGREEMENT = (By.CSS_SELECTOR, '[class="css-1t4dsq5 e1is4j843"]')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '[data-testid="registration-button"]')
    RECAPTCHA_FORM = (By.CSS_SELECTOR, '#recaptcha-token')
    CONFIRM_REGISTRATION_CODE = (By.CSS_SELECTOR, '[data-testid = "code-confirmation-prompt"]')








