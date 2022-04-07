import pytest

from pages.main_page import MainPage
from config import gen_random_string
# 19 тестов
#1
@pytest.mark.smoke
def test_app_is_available(driver):
    page = MainPage(driver)
    assert page.get_title() == "Лабиринт | Книжный интернет-магазин: купить книги, новинки, бестселлеры"

#2
@pytest.mark.smoke
def test_page_not_found(driver):
    page = MainPage(driver, url=r"https://www.labirint.ru/not_there/")
    assert page.get_title() == "Ошибка 404. Интернет-магазин Лабиринт."

#3
def test_is_there_logo(driver):
    page = MainPage(driver)
    assert page.logo.is_presented()

#4
def test_is_there_search_field(driver):
    page = MainPage(driver)
    assert page.search.is_presented()

#5
def test_is_there_messages_button(driver):
    page = MainPage(driver)
    assert page.messages_button.is_presented()

#6
def test_is_there_my_labirint_button(driver):
    page = MainPage(driver)
    assert page.my_labirint_button.is_presented()

#7
def test_is_there_postponed_button(driver):
    page = MainPage(driver)
    assert page.postponed_button.is_presented()

#8
def test_is_there_cart_button(driver):
    page = MainPage(driver)
    assert page.cart_button.is_presented()

#9
def test_is_there_contact_header_button(driver):
    page = MainPage(driver)
    assert page.contact_header_button.is_presented()

#10
def test_is_there_support_header_button(driver):
    page = MainPage(driver)
    assert page.support_header_button.is_presented()

#11
@pytest.mark.smoke
@pytest.mark.parametrize("book_name", ["Гроза",
                                       "Ешь, молись, люби",
                                       "Божественная комедия",
                                       "Улыбка черного кота",
                                       "Элемент крови"])
def test_search_real_book(driver, book_name):
    page = MainPage(driver)
    page.search = book_name
    page.search_run_button.click()
    assert page.products_titles.count() > 0
    relevant_book = 0
    for title in page.products_titles.get_text():
        if book_name.lower() in title.lower():
            relevant_book += 1
    assert relevant_book > page.products_titles.count() * 0.5

#12
def test_empty_search(driver):
    page = MainPage(driver)
    page.search_run_button.click()
    assert driver.title == "Лабиринт | Книжный интернет-магазин: купить книги, новинки, бестселлеры"

#13
def test_whitespace_search(driver):
    page = MainPage(driver)
    page.search = "   "
    page.search_run_button.click()
    assert page.search_error.is_presented()

#14
def test_abracadabra_search(driver):
    page = MainPage(driver)
    page.search = "<j;tcndtyyfz rjvtlbz"
    page.search_run_button.click()
    assert page.search_error.is_presented()

#15
@pytest.mark.parametrize ("wrong_book_name, book_name", [["Груза",
                                                         "Божественная камедии",
                                                         "Бажест камедия",
                                                         "ещьмолись люби",
                                                         "Улыбока черного кота"]])
def test_misspell_search(driver, wrong_book_name, book_name):
    page = MainPage(driver)
    page.search = wrong_book_name
    page.search_run_button.click()
    assert page.products_titles.count() > 0
    # for title in page.products_titles.get_text()[:int(page.products_titles.count()*0.5)]:
    #     msg = f'Wrong product in search "{title}"'
    #     assert book_name in title.lower(), msg
    relevant_book = 0
    for title in page.products_titles.get_text():
        if book_name.lower() in title.lower():
            relevant_book += 1
    assert relevant_book > page.products_titles.count() * 0.5

#16
def test_string_255_search(driver):
    page = MainPage(driver)
    page.search = gen_random_string(255)
    page.search_run_button.click()
    assert page.search_error.is_presented()

#17
def test_string_over9000_search(driver):
    page = MainPage(driver)
    page.search = gen_random_string(9001)
    page.search_run_button.click()
    assert page.search_error.is_presented()

#18
@pytest.mark.parametrize("author_name", ["Мопассан", "Данте", "Олег Рой"])
def test_by_author_search(driver, author_name):
    page = MainPage(driver)
    page.search = author_name
    page.search_run_button.click()
    assert page.products_titles.count() > 0
    relevant_book = 0
    for title in page.products_titles.get_text():
        if author_name.lower() in title.lower():
            relevant_book += 1
    assert relevant_book > page.products_titles.count() * 0.

#19
@pytest.mark.parametrize("publisher_name", ["Эксмо", "АСТ", "Пальмира"])
def test_by_publisher_search(driver, publisher_name):
    page = MainPage(driver)
    page.search = publisher_name
    page.search_run_button.click()
    assert page.book_publisher.count() > 0
    relevant_book = 0
    for title in page.products_titles.get_text():
        if publisher_name.lower() in title.lower():
            relevant_book += 1
    assert relevant_book > page.products_titles.count() * 0.5
