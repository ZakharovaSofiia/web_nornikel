import allure
from pages.events_page import EventsPage


@allure.title('Проверка перехода в категорию Афиша')
def test_guest_can_go_to_events_page(browser, get_city):
    link = f'https://{get_city}.city.online'
    events_page = EventsPage(browser, link)
    events_page.open()
    events_page.go_to_events_page()
    events_page.should_be_events_content_is_correct()