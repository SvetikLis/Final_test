from pages.home_page import MainPage
from selenium.webdriver import ActionChains

# 5 тестов
# 1. Логотип
def test_logo(web_browser):
    page = MainPage(web_browser)
    page.logo.click()

    assert page.get_current_url() == 'https://www.labirint.ru/'


# 2. Сообщения


def test_mesages(web_browser):
    page = MainPage(web_browser)
    page.mesages.click()

    assert page.log_in


# 3. Мой лабиринт


def test_my_labirint(web_browser):
    page = MainPage(web_browser)
    page.my_labirint.click()

    assert page.log_in


# 4. Отложено


def test_deferred(web_browser):
    page = MainPage(web_browser)
    page.deferred.click()

    assert page.get_current_url() == 'https://www.labirint.ru/cabinet/putorder/'


# 5. Корзина


def test_cart(web_browser):
    page = MainPage(web_browser)
    page.cart.click()

    assert page.get_current_url() == 'https://www.labirint.ru/cart/'

