import allure
from pages.services_page import ServicesPage


@allure.title('Проверка перехода в категорию карьера')
def test_guest_can_go_to_career_category(browser, get_city):
    link = f'https://{get_city}.city.online'
    services_page = ServicesPage(browser, link)
    services_page.open()
    services_page.go_to_the_services_page()
    services_page.go_to_career_category()
    services_page.should_be_career_content_is_correct()


@allure.title('Проверка перехода в категорию город')
def test_guest_can_go_to_city_category(browser, get_city):
    link = f'https://{get_city}.city.online'
    services_page = ServicesPage(browser, link)
    services_page.open()
    services_page.go_to_the_services_page()
    services_page.go_to_city_category()
    services_page.should_be_city_content_is_correct()


@allure.title('Проверка перехода в категорию образование')
def test_guest_can_go_to_education_category(browser, get_city):
    link = f'https://{get_city}.city.online'
    services_page = ServicesPage(browser, link)
    services_page.open()
    services_page.go_to_the_services_page()
    services_page.go_to_education_category()
    services_page.should_be_education_content_is_correct()


@allure.title('Проверка перехода в категорию развлечения')
def test_guest_can_go_to_entertainment(browser, get_city):
    link = f'https://{get_city}.city.online'
    services_page = ServicesPage(browser, link)
    services_page.open()
    services_page.go_to_the_services_page()
    services_page.go_to_entertainment_category()
    services_page.should_be_entertainment_content_is_correct()


@allure.title('Проверка перехода в категорию здоровье')
def test_guest_can_go_to_health(browser, get_city):
    link = f'https://{get_city}.city.online'
    services_page = ServicesPage(browser, link)
    services_page.open()
    services_page.go_to_the_services_page()
    services_page.go_to_health_category()
    services_page.should_be_health_content_is_correct()


@allure.title('Проверка перехода в категорию другое')
def test_guest_can_go_to_other(browser, get_city):
    link = f'https://{get_city}.city.online'
    services_page = ServicesPage(browser, link)
    services_page.open()
    services_page.go_to_the_services_page()
    services_page.go_to_other_category()
    services_page.should_be_other_content_is_correct()


@allure.title('Проверка перехода на страницу услуг')
def test_guest_can_go_to_services_page(browser, get_city):
    link = f'https://{get_city}.city.online'
    services_page = ServicesPage(browser, link)
    services_page.open()
    services_page.go_to_the_services_page()
    services_page.should_be_services_page()


@allure.title('Проверка перехода в категорию путешествия')
def test_guest_can_go_to_travel_category(browser, get_city):
    link = f'https://{get_city}.city.online'
    services_page = ServicesPage(browser, link)
    services_page.open()
    services_page.go_to_the_services_page()
    services_page.go_to_travel_category()
    services_page.should_be_travel_content_is_correct()


@allure.title('Проверка перехода в категорию транспорт')
def test_guest_can_go_to_transport_category(browser, get_city):
    link = f'https://{get_city}.city.online'
    services_page = ServicesPage(browser, link)
    services_page.open()
    services_page.go_to_the_services_page()
    services_page.go_to_transport_category()
    services_page.should_be_transport_content_is_correct()








