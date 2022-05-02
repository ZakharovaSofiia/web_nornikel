import allure
from pages.services_page import ServicesPage


@allure.title('Проверка перехода на страницу услуг')
def test_guest_can_go_to_services_page(browser, get_city):
    link = f'https://{get_city}.city.online'
    services_page = ServicesPage(browser, link)
    services_page.open()
    services_page.go_to_the_services_page()
    services_page.should_be_services_page()
