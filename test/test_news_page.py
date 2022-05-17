import allure
from pages.news_page import NewsPage


@allure.title('Проверка перехода в категорию ГО.Медиа')
def test_guest_can_go_to_news_page(browser, get_city):
    link = f'https://{get_city}.city.online'
    news_page = NewsPage(browser, link)
    news_page.open()
    news_page.go_to_news_page()
    news_page.should_be_news_content_is_correct()