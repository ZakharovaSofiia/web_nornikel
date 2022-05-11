import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ServicesPage(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)
        self._link_services = (By.CSS_SELECTOR, '[data-testid="header-link-services"]')
        self._page_services = (By.CSS_SELECTOR, '[data-testid="services-page-title"]')
        self._category_city = (By.CSS_SELECTOR, '[data-testid="services-page-service-category-город"]')
        self._category_other = (By.CSS_SELECTOR, '[data-testid="services-page-service-category-другое"]')
        self._category_health = (By.CSS_SELECTOR, '[data-testid="services-page-service-category-здоровье"]')
        self._category_career = (By.CSS_SELECTOR, '[data-testid="services-page-service-category-карьера"]')
        self._category_education = (By.CSS_SELECTOR, '[data-testid="services-page-service-category-образование"]')
        self._category_travel = (By.CSS_SELECTOR, '[data-testid="services-page-service-category-путешествия"]')
        self._category_entertainment = (By.CSS_SELECTOR, '[data-testid="services-page-service-category-развлечения"]')
        self._category_transport = (By.CSS_SELECTOR, '[data-testid="services-page-service-category-транспорт"]')
        self._card_title_tickets_and_hotels = (By.CSS_SELECTOR, '[data-testid="service-page-service-card-title-60"]')
        self._card_title_excursions = (By.CSS_SELECTOR, '[data-testid="service-page-service-card-title-48"]')

    @allure.step('Переход на страницу услуг')
    def go_to_the_services_page(self):
        self.browser.find_element(*self._link_services).click()

    @allure.step('Переход на странице услуг в категорию путешествия')
    def go_to_travel_category(self):
        self.browser.find_elements(*self._category_travel)[1].click()

    @allure.step('Проверка корректности содержимого во вкладке путешествия')
    def should_be_travel_content_is_correct(self):
        assert self.browser.find_element(*self._card_title_tickets_and_hotels).text == 'Билеты и отели', \
            'Не корректный текст в разделе билеты и отели'
        assert self.browser.find_element(*self._card_title_excursions).text == 'Экскурсии', \
            'Не корректный текст в разделе экскурсии'

    @allure.step('Проверка открытия страницы со списком услуг')
    def should_be_services_page(self):
        assert self.browser.find_element(*self._page_services), 'Не отображается страница со списком услуг'
