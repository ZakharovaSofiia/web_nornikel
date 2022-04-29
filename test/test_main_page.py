from pages.locators import LoginPageLocators
from pages.login_page import LoginPage
from pages.main_page import MainPage
import time


def test_guest_can_go_to_login_page(browser, get_city):
    link = f'https://{get_city}.city.online'
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_login_page()
    login_page = LoginPage(browser, link)
    login_page.should_be_register_form()


def test_guest_can_registration_by_email(browser, get_city):
    email = str(time.time()) + '@fakemail.org'
    password = 'Ferrari1992)!'
    link = f'https://{get_city}.city.online'
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_login_page()
    login_page = LoginPage(browser, link)
    registration_link = browser.find_element(*LoginPageLocators.REGISTRATION_BY_EMAIL)
    registration_link.click()
    email_input = browser.find_element(*LoginPageLocators.EMAIL_INPUT)
    email_input.send_keys(email)
    password_input = browser.find_element(*LoginPageLocators.EMAIL_PASSWORD_INPUT)
    password_input.send_keys(password)
    confirm_password_input = browser.find_element(*LoginPageLocators.CONFIRM_EMAIL_PASSWORD_INPUT)
    confirm_password_input.send_keys(password)
    registration_agreement = browser.find_element(*LoginPageLocators.REGISTRATION_AGREEMENT)
    registration_agreement.click()
    registration_button = browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
    registration_button.click()
    login_page.should_be_confirm_registration_form()



