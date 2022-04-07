import random
import string

url_main_page = 'https://www.labirint.ru'
url_auth = 'https://www.labirint.ru/cabinet/'
user_code = '1DDE-4C39-B6AA.'


def gen_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string

from selenium.webdriver.common.by import By


class TestData:
    CHROME_EXECUTABLE_PATH = "/Chrome/chromedriver.exe"
    FIREFOX_EXECUTABLE_PATH = "/Firefox/geckodriver.exe"

    BASE_URL = "https://www.labirint.ru/"

  # CURRENT Region setting
    CITY_TO_SET = "Москва"
    CURRENT_CITY = "Москва"

    CITY_TO_SET_WRONG_LANGUAGE = "Kbgtwr"
    FIRST_CITY_IN_AUTO_ADVICE_IN_CYRILLIC = "Липецк"

    # Data for PostponePage tests
    NUMBER_OF_BOOKS_TO_POSTPONE = 3

    # Successful deletion of postponed books message
    SUCCESSFUL_DELETION = "Выбранные товары удалены!"

    # Successful deletion of books from Basket
    YOUR_BASKET_IS_EMPTY_TEXT = "Ваша корзина пуста. Почему?"

    # Names of attributes
    ATTRIBUTE_ID = "id"
    ATTRIBUTE_TITLE = "title"
    ATTRIBUTE_VALUE = "value"

    # Data for Search page
    AUTHOR_SEARCH = "Ги Де Мопассан"
    SEARCHED_BOOK_NAME = "Гарри Поттер"
    SEARCHED_RUSSIAN_BOOK_NAME_BY_LATIN = "Fkbcf d cnhfyt xeltc"
    EXPECTED_RESULT_BOOK_NAME = "Алиса в стране чудес"

    # Data for Search page filter
    MIN_PRICE = "500"
    MAX_PRICE = "600"

    """CROSS PAGE LOCATORS"""

    # locator for button to close popup which appear after any action ("В Корзину", "ОТЛОЖИТЬ", etc)
    CLOSE_POPUP_ANY_ACTION = (By.XPATH, '//a[@class="b-basket-popinfo-close"]')

    # locator for Basket "Корзина" button at header
    BASKET_BUTTON_AT_HEADER = (By.XPATH, '//a[@class="b-header-b-personal-e-link top-link-main '
                                         'analytics-click-js cart-icon-js"]')
    # locator for Basket "Корзина" counter
    BASKET_COUNTER = (By.XPATH, '//span[@class="b-header-b-personal-e-icon-count-m-cart basket-in-cart-a"]')

