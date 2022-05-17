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
        self._card_title_poster = (By.CSS_SELECTOR, '[data-testid="service-page-service-card-title-67"]')
        self._card_title_media = (By.CSS_SELECTOR, '[data-testid="service-page-service-card-title-65"]')
        self._card_title_opinions = (By.CSS_SELECTOR, '[data-testid="service-page-service-card-title-66"]')
        self._card_title_taxi = (By.CSS_SELECTOR, '[data-testid="service-page-service-card-title-21"]')
        self._card_title_creativity_training = (By.CSS_SELECTOR, '[data-testid="service-page-service-card-title-54"]')
        self._card_title_webinars = (By.CSS_SELECTOR, '[data-testid="service-page-service-card-title-25"]')
        self._card_title_distance_education = (By.CSS_SELECTOR, '[data-testid="service-page-service-card-title-5"]')
        self._card_title_professional_development = (
        By.CSS_SELECTOR, '[data-testid="service-page-service-card-title-28"]')
        self._card_title_professional_retraining = (
        By.CSS_SELECTOR, '[data-testid="service-page-service-card-title-6"]')
        self._card_title_career_advice = (By.CSS_SELECTOR, '[data-testid="service-page-service-card-title-58"]')
        self._card_title_crowdfunding = (By.CSS_SELECTOR, '[data-testid="service-page-service-card-title-43"]')
        self._card_title_job = (By.CSS_SELECTOR, '[data-testid="service-page-service-card-title-22"]')
        self._card_title_selection_psychologist = (
        By.CSS_SELECTOR, '[data-testid="service-page-service-card-title-61"]')
        self._card_title_nutritionist_online = (By.CSS_SELECTOR, '[data-testid="service-page-service-card-title-50"]')
        self._card_title_consultations_of_doctors = (
        By.CSS_SELECTOR, '[data-testid="service-page-service-card-title-4"]')
        self._card_title_health_check = (By.CSS_SELECTOR, '[data-testid="service-page-service-card-title-51"]')
        self._card_title_promotions_and_discounts = (
        By.CSS_SELECTOR, '[data-testid="service-page-service-card-title-49"]')
        self._card_title_ecology_and_volunteering = (
        By.CSS_SELECTOR, '[data-testid="service-page-service-card-title-34"]')
        self._card_title_aggregator = (By.CSS_SELECTOR, '[data-testid="service-page-service-card-title-71"]')
        self._card_title_payments = (By.CSS_SELECTOR, '[data-testid="service-page-service-card-title-8"]')
        self._card_title_private_specialists = (By.CSS_SELECTOR, '[data-testid="service-page-service-card-title-47"]')
        self._promotions_page = (By.XPATH, "//h3[text()='Акции']")

    @allure.step('Переход на странице услуг в категорию карьера')
    def go_to_career_category(self):
        self.wait_element_to_be_clickable(*self._category_career)
        self.browser.find_elements(*self._category_career)[1].click()

    @allure.step('Переход на странице услуг в категорию город')
    def go_to_city_category(self):
        self.browser.find_elements(*self._category_city)[1].click()

    @allure.step('Переход на странице услуг в категорию образование')
    def go_to_education_category(self):
        self.browser.find_elements(*self._category_education)[1].click()

    @allure.step('Переход на странице услуг в категорию развлечения')
    def go_to_entertainment_category(self):
        self.browser.find_elements(*self._category_entertainment)[1].click()

    @allure.step('Переход на страницу услуг в категорию здоровье')
    def go_to_health_category(self):
        self.wait_element_to_be_clickable(*self._category_health)
        self.browser.find_elements(*self._category_health)[1].click()

    @allure.step('Переход на страницу услуг в категорию другое')
    def go_to_other_category(self):
        self.wait_element_to_be_clickable(*self._category_other)
        self.browser.find_elements(*self._category_other)[1].click()

    @allure.step('Переход в "Акции и скидки" на странице услуг в категории город')
    def go_to_promotions_and_discounts(self):
        self.browser.find_element(*self._card_title_promotions_and_discounts).click()

    @allure.step('Переход на страницу услуг')
    def go_to_the_services_page(self):
        self.wait_element_to_be_clickable(*self._link_services)
        self.browser.find_element(*self._link_services).click()

    @allure.step('Переход на странице услуг в категорию путешествия')
    def go_to_travel_category(self):
        self.browser.find_elements(*self._category_travel)[1].click()

    @allure.step('Переход на странице услуг в категорию транспорт')
    def go_to_transport_category(self):
        self.browser.find_elements(*self._category_transport)[1].click()

    @allure.step('Проверка корректности содержимого во вкладке карьера')
    def should_be_career_content_is_correct(self):
        assert self.browser.find_element(*self._card_title_career_advice).text == 'Карьерные консультации', \
            'Не корректный текст в разделе карьерные консультации'
        assert self.browser.find_element(*self._card_title_crowdfunding).text == 'Краудфандинг', \
            'Не корректный текст в разделе краудфандинг'
        assert self.browser.find_element(*self._card_title_job).text == 'Работа', \
            'Не корректный текст в разделе работа'

    @allure.step('Проверка корректности содержимого во вкладке город')
    def should_be_city_content_is_correct(self):
        assert self.browser.find_element(*self._card_title_promotions_and_discounts).text == 'Акции и скидки', \
            'Не корректный текст в разделе акции и скидки'
        assert self.browser.find_element(*self._card_title_ecology_and_volunteering).text == 'Экология и волонтерство', \
            'Не корректный текст в разделе экология и волонтерство'

    @allure.step('Проверка корректности содержимого во вкладке образование')
    def should_be_education_content_is_correct(self):
        assert self.browser.find_element(*self._card_title_creativity_training).text == 'Тренировка креативности', \
            'Не корректный текст в разделе тренировка креативности'
        assert self.browser.find_element(*self._card_title_webinars).text == 'Вебинары для малого и среднего бизнеса', \
            'Не корректный текст в разделе вебинары для малого и среднего бизнеса'
        assert self.browser.find_element(*self._card_title_distance_education).text == 'Дистанционное образование', \
            'Не корректный текст в разделе дистанционное образование'
        assert self.browser.find_element(*self._card_title_professional_development).text == 'Повышение квалификации', \
            'Не корректный текст в разделе повышение квалификации'
        assert self.browser.find_element(
            *self._card_title_professional_retraining).text == 'Профессиональная переподготовка', \
            'Не корректный текст в разделе профессиональная переподготовка'

    @allure.step('Проверка корректности содержимого во вкладке развлечения')
    def should_be_entertainment_content_is_correct(self):
        assert self.browser.find_element(*self._card_title_poster).text == 'Афиша', \
            'Не корректный текст в разделе афиша'
        assert self.browser.find_element(*self._card_title_media).text == 'ГО.Медиа', \
            'Не корректный текст в разделе ГО.Медиа'
        assert self.browser.find_element(*self._card_title_opinions).text == 'Мнения', \
            'Не корректный текст в разделе мнения'

    @allure.step('Проверка корректности содержимого во вкладке образование')
    def should_be_health_content_is_correct(self):
        assert self.browser.find_element(*self._card_title_selection_psychologist).text == 'Подбор лучшего психолога', \
            'Не корректный текст в разделе подбор лучшего психолога'
        assert self.browser.find_element(*self._card_title_nutritionist_online).text == 'Диетолог онлайн', \
            'Не корректный текст в разделе диетолог онлайн'
        assert self.browser.find_element(*self._card_title_consultations_of_doctors).text == 'Консультации врачей', \
            'Не корректный текст в разделе консультации врачей'
        assert self.browser.find_element(*self._card_title_health_check).text == 'Проверка здоровья', \
            'Не корректный текст в разделе проверка здоровья'

    @allure.step('Проверка корректности содержимого во вкладке другое')
    def should_be_other_content_is_correct(self):
        assert self.browser.find_element(*self._card_title_aggregator).text == 'Агрегатор досок объявлений', \
            'Не корректный текст в разделе Агрегатор досок объявлений'
        assert self.browser.find_element(*self._card_title_payments).text == 'Платежи', \
            'Не корректный текст в разделе Платежи'
        assert self.browser.find_element(*self._card_title_private_specialists).text == 'Частные специалисты', \
            'Не корректный текст в разделе Частные специалисты'

    @allure.step('Проверка корректности содержимого в "Акциях и скидках"')
    def should_be_promotions_and_discounts_content_is_correct(self):
        assert self.browser.find_element(*self._promotions_page).text == 'Акции', \
            'Не корректный текст в Акциях и скидках'

    @allure.step('Проверка открытия страницы со списком услуг')
    def should_be_services_page(self):
        assert self.browser.find_element(*self._page_services), 'Не отображается страница со списком услуг'

    @allure.step('Проверка корректности содержимого во вкладке путешествия')
    def should_be_travel_content_is_correct(self):
        assert self.browser.find_element(*self._card_title_tickets_and_hotels).text == 'Билеты и отели', \
            'Не корректный текст в разделе билеты и отели'
        assert self.browser.find_element(*self._card_title_excursions).text == 'Экскурсии', \
            'Не корректный текст в разделе экскурсии'

    @allure.step('Проверка корректности содержимого во вкладке транспорт')
    def should_be_transport_content_is_correct(self):
        assert self.browser.find_element(*self._card_title_taxi).text == 'Справочник такси', \
            'Не корректный текст в разделе справочник такси'
