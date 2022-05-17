import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class EventsPage(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)
        self._link_events = (By.CSS_SELECTOR, '[data-testid="header-link-events"]')
        self._page_events = (By.CSS_SELECTOR, '[data-testid="events-page-poster-heading"]')

    @allure.step('Переход на страницу Афиша')
    def go_to_events_page(self):
        self.browser.find_element(*self._link_events).click()

    @allure.step('Проверка корректности содержимого во вкладке Афиша')
    def should_be_events_content_is_correct(self):
        assert self.browser.find_element(*self._page_events).text == 'Афиша', \
            'Не корректный заголовок в разделе Афиша'