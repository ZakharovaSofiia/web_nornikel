import allure
from pages.main_page import MainPage
import time


@allure.title('Проверка перехода на страницу логина')
def test_guest_can_go_to_login_page(browser, get_city):
    link = f'https://{get_city}.city.online'
    main_page = MainPage(browser, link)
    main_page.open()
    login_page = main_page.go_to_login_page()
    login_page.should_be_register_form()


@allure.title('Проверка регистрации пользователя')
def test_guest_can_registration_by_email(browser, get_city):
    email = str(time.time()) + '@fakemail.org'
    password = 'Ferrari1992)!'
    link = f'https://{get_city}.city.online'
    main_page = MainPage(browser, link)
    main_page.open()
    login_page = main_page.go_to_login_page()
    login_page.registration_user(email, password)
    login_page.should_be_confirm_registration_form()






