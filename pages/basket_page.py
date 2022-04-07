from selenium.webdriver.common.by import By
from pages.base import WebPage


class BasketPage(WebPage):


    BASKET_URL = "https://www.labirint.ru/cart/"

    # used for test with input quantity into input field
    QUANTITY_TO_ENTER = "11"

    # locator for "Лабиринт" logo by which we can return at home page
    LABIRINT_MAIN_LOGO = (By.XPATH, '//a[@title="Лабиринт - самый большой книжный интернет магазин"]')

    # locator for button  "В КОРЗИНУ" placed under each book
    MOVE_BOOK_TO_BASKET = (By.XPATH, '//a[@class="btn buy-link btn-primary" and contains(text(), "В КОРЗИНУ")]')
    # locator for book price
    BOOK_PRICE_STRING = (By.XPATH, '//span[@class="price-val"]')
    # locator for final sum of books purchased at the Basket page
    PURCHASE_FINAL_SUM = (By.ID, "basket-default-sumprice-discount")
    # locator for button "Очистить корзину" at Basket page
    REMOVE_ALL_GOODS_IN_BASKET = (By.XPATH, '//a[@class="b-link-popup" and contains(text(), "Очистить корзину")]')
    # locator for text "Ваша корзина пуста. Почему?" which show that Basket is empty
    BASKET_IS_EMPTY = (By.XPATH, '//span[@class="g-alttext-small g-alttext-grey g-alttext-head" and contains(text(), '
                                 '"Ваша корзина пуста. Почему?")]')
    # locator for popup window with button "Оформить"
    POPUP_CHECKOUT_BOOK_BUTTON = (By.XPATH, '//a[@class="color_white btn btn-small btn-primary basket-go '
                                            'analytics-click-js"]')
    # locator of input field for quantity of each item (book) in user order at Basket page which is displayed below
    # of each item in Basket
    QUANTITY_OF_EACH_ITEM_IN_BASKET = (By.XPATH, '//input[@class="quantity"]')
    # locator of button "+" increase quantity of item (book) in purchase at Basket page
    INCREASE_QUANTITY_OF_ITEM = (By.XPATH, '//span[@class="btn btn-increase btn-increase-cart"]')
    # locator of button "-" decrease quantity of item (book) in purchase at Basket page
    DECREASE_QUANTITY_OF_ITEM = (By.XPATH, '//span[@class="btn btn-lessen btn-lessen-cart"]')
    # locator of button "Начать оформление" (small one) which is at right side of the Basket page
    START_CHECKOUT = (By.XPATH, '//input[@class="btn btn-small btn-more"]')
    # locator of button "Оформить и оплатить" at Checkout page
    CHECKOUT_AND_PAY = (By.XPATH, '//input[@value="Оформить и оплатить"]')




    def price_by_int(self, element):
        element_text = element.text
        price_string = element_text.replace(' ', '').replace('₽', '')
        return int(price_string)


