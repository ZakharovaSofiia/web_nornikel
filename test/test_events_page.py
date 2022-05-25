import allure
from pages.events_page import EventsPage


@allure.title('Проверка перехода в раздел Город страницы Афиша')
def test_guest_can_go_to_city(browser, get_city):
    link = f'https://{get_city}.city.online'
    events_page = EventsPage(browser, link)
    events_page.open()
    events_page.go_to_events_page()
    events_page.go_to_city_page()
    events_page.should_be_dates_events_content_is_correct()


@allure.title('Проверка перехода в раздел Конкурсы страницы Афиша')
def test_guest_can_go_to_contests(browser, get_city):
    link = f'https://{get_city}.city.online'
    events_page = EventsPage(browser, link)
    events_page.open()
    events_page.go_to_events_page()
    events_page.go_to_contests_page()
    events_page.should_be_dates_events_content_is_correct()


@allure.title('Проверка перехода на страницу Афиша')
def test_guest_can_go_to_events_page(browser, get_city):
    link = f'https://{get_city}.city.online'
    events_page = EventsPage(browser, link)
    events_page.open()
    events_page.go_to_events_page()
    events_page.should_be_events_content_is_correct()


@allure.title('Проверка перехода в раздел Выставки страницы Афиша')
def test_guest_can_go_to_exhibitions(browser, get_city):
    link = f'https://{get_city}.city.online'
    events_page = EventsPage(browser, link)
    events_page.open()
    events_page.go_to_events_page()
    events_page.go_to_exhibitions_page()
    events_page.should_be_dates_events_content_is_correct()


@allure.title('Проверка перехода в раздел Фестивали страницы Афиша')
def test_guest_can_go_to_festivals(browser, get_city):
    link = f'https://{get_city}.city.online'
    events_page = EventsPage(browser, link)
    events_page.open()
    events_page.go_to_events_page()
    events_page.go_to_festivals_page()
    events_page.should_be_dates_events_content_is_correct()


@allure.title('Проверка перехода в раздел Для детей страницы Афиша')
def test_guest_can_go_to_for_children(browser, get_city):
    link = f'https://{get_city}.city.online'
    events_page = EventsPage(browser, link)
    events_page.open()
    events_page.go_to_events_page()
    events_page.go_to_for_children_page()
    events_page.should_be_dates_events_content_is_correct()


@allure.title('Проверка перехода в раздел Онлайн страницы Афиша')
def test_guest_can_go_to_online(browser, get_city):
    link = f'https://{get_city}.city.online'
    events_page = EventsPage(browser, link)
    events_page.open()
    events_page.go_to_events_page()
    events_page.go_to_online_page()
    events_page.should_be_dates_events_content_is_correct()


@allure.title('Проверка перехода в раздел Мастер-классы страницы Афиша')
def test_guest_can_go_to_master_classes(browser, get_city):
    link = f'https://{get_city}.city.online'
    events_page = EventsPage(browser, link)
    events_page.open()
    events_page.go_to_events_page()
    events_page.go_to_master_classes_page()
    events_page.should_be_dates_events_content_is_correct()


@allure.title('Проверка перехода в раздел Встречи страницы Афиша')
def test_guest_can_go_to_meetings(browser, get_city):
    link = f'https://{get_city}.city.online'
    events_page = EventsPage(browser, link)
    events_page.open()
    events_page.go_to_events_page()
    events_page.go_to_meetings_page()
    events_page.should_be_dates_events_content_is_correct()


@allure.title('Проверка перехода в раздел Акции страницы Афиша')
def test_guest_can_go_to_promotions(browser, get_city):
    link = f'https://{get_city}.city.online'
    events_page = EventsPage(browser, link)
    events_page.open()
    events_page.go_to_events_page()
    events_page.go_to_promotions_page()
    events_page.should_be_dates_events_content_is_correct()

