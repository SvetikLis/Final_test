
import os
from pages.base import WebPage
from pages.elements import WebElement


class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'

        super().__init__(web_driver, url)

    search_field = WebElement(id='search-field')
    search_button = WebElement(xpath='//button[@type="submit"]')
    message_search = WebElement(xpath='//h1[@class="index-top-title"]')
    deferred_button = WebElement(xpath='//*[@class="b-header-b-personal-e-icon '
                                       'b-header-b-personal-e-icon-m-putorder b-header-e-sprite-background"]')
    button_cart = WebElement(xpath='//*[@class="b-header-b-personal-e-icon b-header-b-personal-e-icon-m-cart  '
                                   'b-header-e-sprite-background"]')
    auth_field = WebElement(xpath='/html/body/div[1]/div[1]/div/div/div/div/div[1]/form[1]/div[3]/input')
    auth_btn = WebElement(xpath='//*[@id="g-recap-0-btn"]')
    main_page_btn = WebElement(xpath='//*[@id="minwidth"]/div[5]/div/div[1]/div[1]/div/a[1]/span')
    close_btn = WebElement(xpath='//*[@id="auth-success-login"]/input[2]')
    button_my_maze = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/a[1]')
    button_shipping_and_payment = WebElement(xpath='//a[@href="/help/"]')
    button_cert = WebElement(xpath='//a[@href="/top/certificates/"]')
    button_ratings = WebElement(xpath='//a[@href="/rating/?id_genre=-1&nrd=1"]')
    button_new_products = WebElement(xpath='//a[@href="/novelty/"]')
    button_discount = WebElement(xpath='//a[@href="/sale/"]')
    button_contact = WebElement(xpath='//*[@data-event-content="Контакты"]')
    button_support = WebElement(xpath='//a[@href="/support/"]')
    button_maps = WebElement(xpath='//a[@href="/maps/"]')
    region = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[1]/div[4]/div/div[1]/ul/li[12]/span[1]/'
                              'span/span[3]/span')
    field_region = WebElement(xpath='//*[@id="region-post"]')
    region_click = WebElement(xpath='//*[@id="minwidth"]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/h2[1]')
    message_region = WebElement(xpath='//span[@title="Москва"]')
    more_books_with_discounts = WebElement(xpath='//*[@class="btn btn-not-avaliable autodiscounts__btn '
                                                 'autodiscounts__padding"]')
    vk_footer = WebElement(xpath='//a[@data-event-content="ВКонтакте"]')
    vk_child_footer = WebElement(xpath='//a[@data-event-content="ВКонтакте. Дети"]')
    youtube_footer = WebElement(xpath='//a[@data-event-content="Ютьюб"]')
    instagram_footer = WebElement(xpath='//a[@data-event-content="Инстаграм"]')
    instagram_child_footer = WebElement(xpath='//a[@data-event-content="Инстаграм. Дети"]')
    facebook_footer = WebElement(xpath='//a[@data-event-content="Фейсбук"]')
    ok_footer = WebElement(xpath='//a[@data-event-content="Одноклассники"]')
    twitter_footer = WebElement(xpath='//a[@data-event-content="Твиттер"]')
    zen_footer = WebElement(xpath='//a[@data-event-content="Дзен"]')
    telegram_footer = WebElement(xpath='//a[@data-event-content="Телеграм"]')
    tiktok_footer = WebElement(xpath='//a[@data-event-content="ТикТок"]')
    more = WebElement(xpath='//*[@data-tooltip_title="Еще действия"]''[1]')
    compare = WebElement(xpath='//*[@class="b-list-item-hover js-card-block-actions-compare"]')
    message_compare = WebElement(xpath='//span[Compare(test()), "1") and @class="cabinet-menu__counter"]')
    buy = WebElement(xpath='//*[@class="btn buy-link btn-primary"]')
    message_buy = WebElement(xpath='//span[Compare(test()), "1") and @class="b-header-b-personal-e-icon-count-m-cart '
                                   'basket-in-cart-a"]')