import os
from pages.base import WebPage
from pages.elements import WebElement


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'

        super().__init__(web_driver, url)



    login_field = WebElement(xpath='//*[@class="full-input__input formvalidate-error"]')
    enter = WebElement(xpath='//*[@id="g-recap-0-btn"]')
    automatic_closing = WebElement(xpath='//*[@id="auth-success-login"]/input[2]')
    auth_error = WebElement(xpath='//a[contains(text(),"Введенного кода не существует")]')
    auth_error_2 = WebElement(xpath='//span[contains(text(),"Нельзя использовать символ «{N}»")]')



    logo = WebElement(xpath='//*[@class="b-header-b-logo-e-logo-wrap"]')
    winter_sale = WebElement(xpath='//*[@class="b-header-b-logo-e-discount"]')
    mesages = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[1]/div[2]/div/ul/li[3]/a/span[1]/span')
    log_in = WebElement(xpath='//span[contains(text(),"Введите свой код скидки, телефон или эл.почту")]')
    my_labirint = WebElement(xpath='//*[@id="minwidth"]/div[5]/div/div[1]/div[2]/div/ul/li[4]/a/span[2]')
    deferred = WebElement(xpath='//*[@class="b-header-b-personal-e-link top-link-main top-link-main_putorder"]')
    cart = WebElement(xpath='//*[@class="b-header-b-personal-e-list-item have-dropdown  last-child"]')
    plus_18 = WebElement(xpath='//*[@class="b-header-e-icon-adult b-header-e-icon-adult-m-big '
                               'b-header-e-sprite-background"]')
    header_books = WebElement(xpath='//span[@class="b-header-b-menu-e-link top-link-menu first-child"]')
    header_main_2021 = WebElement(xpath='//*[@id="minwidth"]/div[5]/div/div[1]/div[4]/div/div[1]/ul/li[2]/span/a')
    header_school = WebElement(xpath='//*[@id="minwidth"]/div[5]/div/div[1]/div[4]/div/div[1]/ul/li[3]/span/a')
    header_toys = WebElement(xpath='//*[@id="minwidth"]/div[5]/div/div[1]/div[4]/div/div[1]/ul/li[4]/span/a')
    header_office = WebElement(xpath='//*[@id="minwidth"]/div[5]/div/div[1]/div[4]/div/div[1]/ul/li[5]/span/a')
    header_club = WebElement(xpath='//*[@id="minwidth"]/div[5]/div/div[1]/div[4]/div/div[1]/ul/li[11]/span/a')
    delivery_and_payment = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div/ul/li[1]/a')
    certificates = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div/ul/li[2]/a')
    rating = WebElement(xpath='//a[@href="/rating/?id_genre=-1&nrd=1"]')
    new_books = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div/ul/li[4]/a')
    discount = WebElement(xpath='//a[@href="/sale/"]')
    contacts = WebElement(xpath='//*[@data-event-content="Контакты"]')
    support = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div/ul/li[10]/a')
    maps = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div/ul/li[11]/a')



    search = WebElement(id='search-field')
    search_btn = WebElement(xpath='//button[@type="submit"]')
    successful_search = WebElement(xpath='//span[contains(text(),"Все, что мы нашли в Лабиринте по запросу")]')
    not_successful_search = WebElement(xpath='//h1[contains(text(),"Мы ничего не нашли по вашему запросу! Что '
                                             'делать?")]')
    all_filers = WebElement(xpath='//span[contains(text(), "ВСЕ ФИЛЬТРЫ") and @class="navisort-item__content"]')
    reset_all_filers = WebElement(xpath='//*[@id="rubric-tab"]/div[2]/div[1]/div/div[2]/div/span[3]')
    available = WebElement(xpath='//*[@id="section-search-form"]/div[2]/div[2]/div[1]/label[1]/span[2]')
    not_available = WebElement(xpath='//*[@id="section-search-form"]/div[2]/div[2]/div[4]/label[1]/span[2]')
    show_all_found = WebElement(xpath='//input[@class="show-goods__button"]')



    best_sale = WebElement(xpath='//a[@href="/best/sale/"]')
    random_book = WebElement(xpath='//*[@id="catalog"]/div/div[3]/div/div[4]/div/div[1]/div/div[1]/div/div[1]')
    random_book_1 = WebElement(xpath='//*[@id="catalog"]/div/div[3]/div/div[4]/div/div[3]/div/div[1]/div/div[1]')
    buy_book = WebElement(xpath='//*[@class="btn btn-small btn-primary btn-buy"]')
    successfuly_odered = WebElement(xpath='//span[contains(text(),"Ваш заказ")]')
    add_to_deferred = WebElement(xpath='//a[@class="fave"]')
    successfuly_deferred = WebElement(xpath='//a[@title="Выделить все отложенные товары"]')
    compare = WebElement(xpath='//a[@title="Добавить к сравнению"]')
    successfuly_compared = WebElement(xpath='//*[@class="compare big-compare done"]')
    compare_books = WebElement(xpath='//a[@href="/compare/"]')



    plus_one_more = WebElement(xpath='//span[@class="btn btn-increase btn-increase-cart"]')
    remove_from_cart = WebElement(xpath='//span[@class="btn btn-lessen btn-lessen-cart"]')
    two_books_in_cart = WebElement(xpath='//input[Compare(test()), "2") and @class="quantity"]')
    empty_cart = WebElement(xpath='//span[contains(text(),"Ваша корзина пуста. Почему?"]')
    btn_ok_close = WebElement(xpath='//span[@class="fright btn btn-primary btn-middle"]')