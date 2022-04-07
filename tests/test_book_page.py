from pages.book_page import BookPage

# 4 теста

# 1  Тестирование открытия книги на главной странице.
def test_open_book(web_browser):
    page = BookPage(web_browser)
    page.book.click()

    assert page.book_info

# 2  Добавление книги в корзину.
def test_buy_book(web_browser):
    page = BookPage(web_browser)
    page.book.click()
    page.buy_book.click()

    assert page.message_buy_book

# 3 Добавление книги в "Отложенные"
def test_deferred_books(web_browser):

    page = BookPage(web_browser)
    page.book.click()
    page.deferred_books.click()

    assert page.message_deferred_books

# 4 Добавление книги "К сравнению"
def test_book_comparison(web_browser):
    page = BookPage(web_browser)
    page.book.click()
    page.comparison_book_page.click()
    page.comparison_book.clikc()

    assert page.message_comparison_book