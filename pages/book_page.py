import os
from pages.base import WebPage
from pages.elements import WebElement


class BookPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'

        super().__init__(web_driver, url)

    book = WebElement(xpath='//*[@class="card-column card-column_gutter-60 swiper-slide swiper-slide-active"]')
    book_info = WebElement(xpath='//*[@class="prodtitle"]')
    buy_book = WebElement(xpath='//*[@class="btn btn-small btn-primary btn-buy"]')
    message_buy_book = WebElement(xpath='//span[Compare(test()), "1") and '
                                        '@class="b-header-b-personal-e-icon-count-m-cart basket-in-cart-a"]')
    deferred_books = WebElement(xpath='//a[@class="fave"]')
    message_deferred_books = WebElement(xpath='//span[Compare(test()), "1") and '
                                              '@class="b-header-b-personal-e-icon-count-m-putorder '
                                              'basket-in-dreambox-a"]')
    comparison_book_page = WebElement(xpath='//*[@class="compare big-compare"]')
    comparison_book = WebElement(xpath='//*[@class="compare big-compare done"]')
    message_comparison_book = WebElement(xpath='//span[Compare(test()), "1") and @class="cabinet-menu__counter"]')