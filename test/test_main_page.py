from pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = 'https://monchegorsk.city.online'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()