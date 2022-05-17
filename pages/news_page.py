import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class NewsPage(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)
        self._link_news = (By.CSS_SELECTOR, '[data-testid="header-link-news"]')
        self._page_news = (By.CSS_SELECTOR, '[data-testid="news-page-news-heading"]')

    @allure.step('Переход на страницу ГО.Медиа')
    def go_to_news_page(self):
        self.browser.find_element(*self._link_news).click()

    @allure.step('Проверка корректности содержимого во вкладке ГО.Медиа')
    def should_be_news_content_is_correct(self):
        assert self.browser.find_element(*self._page_news).text == 'ГО.Медиа', \
            'Не корректный заголовок в разделе ГО.Медиа'