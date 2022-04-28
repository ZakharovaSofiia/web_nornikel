from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser, get_city):
    link = f'https://{get_city}.city.online'
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_login_page()
    login_page = LoginPage(browser, link)
    login_page.should_be_register_form()

