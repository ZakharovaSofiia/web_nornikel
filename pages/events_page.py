import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class EventsPage(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)
        self._link_events = (By.CSS_SELECTOR, '[data-testid="header-link-events"]')
        self._page_events = (By.CSS_SELECTOR, '[data-testid="events-page-poster-heading"]')
        self._events_promotions = (By.CSS_SELECTOR, '[data-testid="events-page-type-146"]')
        self._events_meetings = (By.CSS_SELECTOR, '[data-testid="events-page-type-44"]')
        self._events_exhibitions = (By.CSS_SELECTOR, '[data-testid="events-page-type-42"]')
        self._events_city = (By.CSS_SELECTOR, '[data-testid="events-page-type-151"]')
        self._events_for_children = (By.CSS_SELECTOR, '[data-testid="events-page-type-148"]')
        self._events_contests = (By.CSS_SELECTOR, '[data-testid="events-page-type-7"]')
        self._events_concerts = (By.CSS_SELECTOR, '[data-testid="events-page-type-8"]')
        self._events_master_classes = (By.CSS_SELECTOR, '[data-testid="events-page-type-150"]')
        self._events_online = (By.CSS_SELECTOR, '[data-testid="events-page-type-43"]')
        self._events_performances = (By.CSS_SELECTOR, '[data-testid="events-page-type-80"]')
        self._events_festivals = (By.CSS_SELECTOR, '[data-testid="events-page-type-6"]')
        self._events_all_dates = (By.CSS_SELECTOR, '[data-testid="events-page-data-filter-0"]')
        self._events_today = (By.CSS_SELECTOR, '[data-testid="events-page-data-filter-1"]')
        self._events_tomorrow = (By.CSS_SELECTOR, '[data-testid="events-page-data-filter-2"]')
        self._events_on_the_weekend = (By.CSS_SELECTOR, '[data-testid="events-page-data-filter-3"]')
        self._events_choose_period = (By.CSS_SELECTOR, '[data-testid="events-page-data-filter-4"]')

    @allure.step('Переход в Город страницы Афиша')
    def go_to_city_page(self):
        self.browser.find_element(*self._events_city).click()

    @allure.step('Переход в Конкурсы страницы Афиша')
    def go_to_contests_page(self):
        self.browser.find_element(*self._events_contests).click()

    @allure.step('Переход на страницу Афиша')
    def go_to_events_page(self):
        self.browser.find_element(*self._link_events).click()

    @allure.step('Переход в Выставки страницы Афиша')
    def go_to_exhibitions_page(self):
        self.browser.find_element(*self._events_exhibitions).click()

    @allure.step('Переход в Фестивали страницы Афиша')
    def go_to_festivals_page(self):
        self.browser.find_element(*self._events_festivals).click()

    @allure.step('Переход в Для детей страницы Афиша')
    def go_to_for_children_page(self):
        self.browser.find_element(*self._events_for_children).click()

    @allure.step('Переход в Мастер-классы страницы Афиша')
    def go_to_master_classes_page(self):
        self.browser.find_element(*self._events_master_classes).click()

    @allure.step('Переход во Встречи страницы Афиша')
    def go_to_meetings_page(self):
        self.browser.find_element(*self._events_meetings).click()

    @allure.step('Переход в Онлайн страницы Афиша')
    def go_to_online_page(self):
        self.browser.find_element(*self._events_online).click()

    @allure.step('Переход в Акции страницы Афиша')
    def go_to_promotions_page(self):
        self.browser.find_element(*self._events_promotions).click()

    @allure.step('Проверка корректности содержимого во вкладке Афиша')
    def should_be_events_content_is_correct(self):
        assert self.browser.find_element(*self._page_events).text == 'Афиша', \
            'Не корректный заголовок в разделе Афиша'

    @allure.step('Проверка корректности содержимого в категориях страницы Афиша')
    def should_be_dates_events_content_is_correct(self):
        assert self.browser.find_element(*self._events_all_dates).text == 'Все даты', \
            'Не корректный заголовок в разделе Все даты'
        assert self.browser.find_element(*self._events_today).text == 'Сегодня', \
            'Не корректный заголовок в разделе Сегодня'
        assert self.browser.find_element(*self._events_tomorrow).text == 'Завтра', \
            'Не корректный заголовок в разделе Завтра'
        assert self.browser.find_element(*self._events_on_the_weekend).text == 'В выходные', \
            'Не корректный заголовок в разделе В выходные'
        assert self.browser.find_element(*self._events_choose_period), 'Нет возможности выбрать период'