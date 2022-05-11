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

    @allure.step('Переход на страницу услуг')
    def go_to_the_services_page(self):
        self.browser.find_element(*self._link_services).click()

    def should_be_services_page(self):
        assert self.browser.find_element(*self._page_services), 'Не отображается страница со списком услуг'
