import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class EventsPage(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)
        self._link_events = (By.CSS_SELECTOR, '[data-testid="header-link-events"]')
        self._page_events = (By.CSS_SELECTOR, '[data-testid="events-page-poster-heading"]')
        self._events_promotions = (By.CSS_SELECTOR, '[data-testid="events-page-type-146"]')
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

    @allure.step('Переход на страницу Афиша')
    def go_to_events_page(self):
        self.browser.find_element(*self._link_events).click()

    @allure.step('Проверка корректности содержимого во вкладке Афиша')
    def should_be_events_content_is_correct(self):
        assert self.browser.find_element(*self._page_events).text == 'Афиша', \
            'Не корректный заголовок в разделе Афиша'