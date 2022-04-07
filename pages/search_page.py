from selenium.webdriver.common.by import By
from config import TestData
from pages.base import WebPage


class SearchPage(WebPage):

    URL = TestData.BASE_URL + "search/"

    LABIRINT_MAIN_LOGO = (By.XPATH, '//span[@class="b-header-b-logo-e-logo"]')

    COOKIES_POLICY_BUTTON = (By.XPATH, '//button[@class="cookie-policy__button js-cookie-policy-agree"]')

    SEARCH_FIELD = (By.ID, "search-field")

    SEARCH_SUBMIT = (By.XPATH, '//button[@class="b-header-b-search-e-btn"]')

    AUTHOR_NAME = (By.XPATH, '//div[@class="product-author"]/a')

    BOOK_DESCRIPTION = (By.XPATH, '//a[@class="product-title-link"]')

    ALL_FILTERS = (By.XPATH, '//span[@class="navisort-item__content" and contains(text(), "ВСЕ ФИЛЬТРЫ")]')
    PAPER_BOOKS_IN_ALL_FILTERS = (By.XPATH, '//span[contains(text(), "Бумажные книги")]')
    DIGITAL_BOOKS_IN_ALL_FILTERS = (By.XPATH, '//span[contains(text(), "Электронные книги")]')
    SHOW_RESULTS = (By.XPATH, '//input[@class="show-goods__button" and @value="Показать"]')
    PRICE_MENU_BUTTON = (By.XPATH, '//div[@class="bl-name" and contains(text(), "ЦЕНА")]')
    SET_MIN_PRICE = (By.ID, "section-search-form-price_min")
    SET_MAX_PRICE = (By.ID, "section-search-form-price_max")

    ENABLED_PAPER_BOOKS = (By.XPATH, '//div[contains(text(), "Бумажные книги")]')
    BOOKS_AVAILABLE_CURRENTLY = (By.XPATH, '//div[@class="filter-reset__content" and contains(text(), "В наличии")]')
    ALL_CURRENT_SETTINGS = (By.XPATH, '//div[@class="filter-reset__content"]')

    DIGITAL_BOOKS_LABEL = (By.XPATH, '//span[@class="card-label__text card-label__text_inversed" and contains(text(), '
                                     '"Электронная книга")]')
    BUY_NOW_BUTTON = (By.XPATH, '//a[@class="btn buy-link js-ebooks-buy-btn btn-primary" and contains(text(), '
                                '"КУПИТЬ")]')

    BOOK_PRICE_STRING = (By.XPATH, '//span[@class="price-val"]/span')
    PAGINATION_PAGE_BUTTON = (By.XPATH, '//a[@class="pagination-next__text" and contains(text(), "Следующая")]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(SearchPage.URL)

    def search_match_fully(self, element, search_name):
        element_text = element.get_attribute(TestData.ATTRIBUTE_TITLE)
        element_in_list = element_text.lower().split()
        name_list = search_name.lower().split()
        result = list(set(element_in_list) & set(name_list))
        return len(name_list) == len(result)

    def price_by_int(self, element):
        element_text = element.text
        price_string = element_text.replace(' ', '').replace('₽', '')
        return int(price_string)