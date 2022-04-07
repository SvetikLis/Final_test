import time
from config import TestData
from pages.basket_page import BasketPage


# 1
def test_first_book_moved_in_basket_and_price_is_same(self):
    self.basketPage = BasketPage(self.driver)
    self.basketPage.accept_cookies_policy()
    self.basketPage.remove_all_good_in_basket_and_reload_page()
    self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
    fist_book_button_move_into_basket = self.list_of_buttons_move_into_basket[0]
    self.list_of_book_prices = self.basketPage.find_several_element(BasketPage.BOOK_PRICE_STRING)
    first_book_price_element = self.list_of_book_prices[0]
    first_book_price = self.basketPage.price_by_int(first_book_price_element)
    fist_book_button_move_into_basket.click()
    self.basketPage.do_click(TestData.CLOSE_POPUP_ANY_ACTION)
    self.basketPage.do_click(TestData.BASKET_BUTTON_AT_HEADER)
    self.list_of_book_prices_in_basket = self.basketPage.find_several_element(BasketPage.BOOK_PRICE_STRING)
    price_of_first_book_string = self.list_of_book_prices_in_basket[0]
    first_book_price_in_basket = self.basketPage.price_by_int(price_of_first_book_string)
    assert first_book_price == first_book_price_in_basket


# 2
def test_that_clear_basket_button_clean_basket(self):
    self.basketPage = BasketPage(self.driver)
    self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
    self.list_of_buttons_move_into_basket[0].click()
    self.basketPage.do_click(TestData.CLOSE_POPUP_ANY_ACTION)
    self.basketPage.do_click(TestData.BASKET_BUTTON_AT_HEADER)
    self.list_of_book_prices_in_basket = self.basketPage.find_several_element(BasketPage.BOOK_PRICE_STRING)
    price_of_first_book_string = self.list_of_book_prices_in_basket[0]
    self.basketPage.do_click(BasketPage.REMOVE_ALL_GOODS_IN_BASKET)
    result = self.basketPage.get_element_text(BasketPage.BASKET_IS_EMPTY)
    assert self.basketPage.element_is_not_visible(price_of_first_book_string)
    assert result.lower() == TestData.YOUR_BASKET_IS_EMPTY_TEXT.lower()


# 3
def test_first_book_moved_in_basket_and_price_is_same_and_equal_final_sum(self):
    self.basketPage = BasketPage(self.driver)
    self.basketPage.remove_all_good_in_basket_and_reload_page()
    self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
    fist_book_button_move_into_basket = self.list_of_buttons_move_into_basket[0]
    self.list_of_book_prices = self.basketPage.find_several_element(BasketPage.BOOK_PRICE_STRING)
    first_book_price_element = self.list_of_book_prices[0]
    first_book_price = self.basketPage.price_by_int(first_book_price_element)
    fist_book_button_move_into_basket.click()
    self.basketPage.do_click(TestData.CLOSE_POPUP_ANY_ACTION)
    self.basketPage.do_click(TestData.BASKET_BUTTON_AT_HEADER)
    self.list_of_book_prices_in_basket = self.basketPage.find_several_element(BasketPage.BOOK_PRICE_STRING)
    price_of_first_book_string = self.list_of_book_prices_in_basket[0]
    first_book_price_in_basket = self.basketPage.price_by_int(price_of_first_book_string)
    final_sum = self.basketPage.get_element_text(BasketPage.PURCHASE_FINAL_SUM).replace(' ', '')
    assert (first_book_price and first_book_price_in_basket) == int(final_sum)


# 4
def test_that_button_in_popup_window_leads_to_basket(self):
    self.basketPage = BasketPage(self.driver)
    self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
    fist_book_button_move_into_basket = self.list_of_buttons_move_into_basket[0]
    fist_book_button_move_into_basket.click()
    self.basketPage.find_several_element(BasketPage.POPUP_CHECKOUT_BOOK_BUTTON)[0].click()
    assert self.basketPage.get_current_url() == BasketPage.BASKET_URL


# 5
def test_that_initial_quantity_of_item_added_in_basket_is_one(self):
    self.basketPage = BasketPage(self.driver)
    self.basketPage.remove_all_good_in_basket_and_reload_page()
    self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
    self.list_of_buttons_move_into_basket[0].click()
    self.basketPage.do_click(TestData.CLOSE_POPUP_ANY_ACTION)
    self.basketPage.do_click(TestData.BASKET_BUTTON_AT_HEADER)
    self.list_of_quantity_of_all_items_in_basket = self.basketPage.find_several_element(
        BasketPage.QUANTITY_OF_EACH_ITEM_IN_BASKET)
    first_book_input_field = self.list_of_quantity_of_all_items_in_basket[0]
    quantity_of_first_book = first_book_input_field.get_attribute(TestData.ATTRIBUTE_VALUE)
    assert int(quantity_of_first_book) == 1


# 6
def test_that_quantity_of_item_added_in_basket_can_be_increased(self):
    self.basketPage = BasketPage(self.driver)
    self.basketPage.remove_all_good_in_basket_and_reload_page()
    self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
    self.list_of_buttons_move_into_basket[0].click()
    self.basketPage.do_click(TestData.CLOSE_POPUP_ANY_ACTION)
    self.basketPage.do_click(TestData.BASKET_BUTTON_AT_HEADER)
    self.list_of_quantity_of_all_items_in_basket = self.basketPage.find_several_element(
        BasketPage.QUANTITY_OF_EACH_ITEM_IN_BASKET)
    first_book_input_field = self.list_of_quantity_of_all_items_in_basket[0]
    quantity_of_first_book = first_book_input_field.get_attribute(TestData.ATTRIBUTE_VALUE)
    self.list_of_increase_buttons = self.basketPage.find_several_element(BasketPage.INCREASE_QUANTITY_OF_ITEM)
    self.list_of_increase_buttons[0].click()
    new_quantity_of_first_book = first_book_input_field.get_attribute(TestData.ATTRIBUTE_VALUE)
    assert int(new_quantity_of_first_book) - int(quantity_of_first_book) == 1


# 7
def test_that_quantity_can_set_by_enter_digits_into_input_field(self):
    self.basketPage = BasketPage(self.driver)
    self.basketPage.remove_all_good_in_basket_and_reload_page()
    self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
    self.list_of_buttons_move_into_basket[0].click()
    self.basketPage.do_click(TestData.CLOSE_POPUP_ANY_ACTION)
    self.basketPage.do_click(TestData.BASKET_BUTTON_AT_HEADER)
    self.list_of_quantity_of_all_items_in_basket = self.basketPage.find_several_element(
        BasketPage.QUANTITY_OF_EACH_ITEM_IN_BASKET)
    first_book_input_field = self.list_of_quantity_of_all_items_in_basket[0]
    quantity_of_first_book = first_book_input_field.get_attribute(TestData.ATTRIBUTE_VALUE)
    self.basketPage.clear_text_in_element_and_send_text_with_enter(
        first_book_input_field, BasketPage.QUANTITY_TO_ENTER)
    new_quantity_of_first_book = first_book_input_field.get_attribute(TestData.ATTRIBUTE_VALUE)
    assert int(quantity_of_first_book) == 1
    assert int(new_quantity_of_first_book) == int(BasketPage.QUANTITY_TO_ENTER)


# 8
def test_that_quantity_can_decreased_by_pressing_decrease_button(self):
    self.basketPage = BasketPage(self.driver)
    self.basketPage.remove_all_good_in_basket_and_reload_page()
    self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
    self.list_of_buttons_move_into_basket[0].click()
    self.basketPage.do_click(TestData.CLOSE_POPUP_ANY_ACTION)
    self.basketPage.do_click(TestData.BASKET_BUTTON_AT_HEADER)
    self.list_of_quantity_of_all_items_in_basket = self.basketPage.find_several_element(
        BasketPage.QUANTITY_OF_EACH_ITEM_IN_BASKET)
    first_book_input_field = self.list_of_quantity_of_all_items_in_basket[0]
    self.basketPage.clear_text_in_element_and_send_text_with_enter(
        first_book_input_field, BasketPage.QUANTITY_TO_ENTER)
    quantity_of_first_book = first_book_input_field.get_attribute(TestData.ATTRIBUTE_VALUE)
    self.list_of_increase_buttons = self.basketPage.find_several_element(BasketPage.DECREASE_QUANTITY_OF_ITEM)
    self.list_of_increase_buttons[0].click()
    new_quantity_of_first_book = first_book_input_field.get_attribute(TestData.ATTRIBUTE_VALUE)
    assert int(quantity_of_first_book) - int(new_quantity_of_first_book) == 1


# 9
def test_that_sum_will_raise_accordingly_when_quantity_of_item_increased(self):
    self.basketPage = BasketPage(self.driver)
    self.basketPage.remove_all_good_in_basket_and_reload_page()
    self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
    self.list_of_buttons_move_into_basket[0].click()
    self.basketPage.do_click(TestData.CLOSE_POPUP_ANY_ACTION)
    self.basketPage.do_click(TestData.BASKET_BUTTON_AT_HEADER)
    self.list_of_quantity_of_all_items_in_basket = self.basketPage.find_several_element(
        BasketPage.QUANTITY_OF_EACH_ITEM_IN_BASKET)
    self.list_of_book_prices_in_basket = self.basketPage.find_several_element(BasketPage.BOOK_PRICE_STRING)
    price_of_first_book_string = self.list_of_book_prices_in_basket[0]
    first_book_price_in_basket = self.basketPage.price_by_int(price_of_first_book_string)
    first_book_input_field = self.list_of_quantity_of_all_items_in_basket[0]
    self.basketPage.clear_text_in_element_and_send_text_with_enter(
        first_book_input_field, BasketPage.QUANTITY_TO_ENTER)
    time.sleep(5)
    self.list_of_book_prices_in_basket_new = self.basketPage.find_several_element(BasketPage.BOOK_PRICE_STRING)
    price_of_first_item = self.list_of_book_prices_in_basket_new[0]
    new_price = self.basketPage.price_by_int(price_of_first_item)
    assert (first_book_price_in_basket * int(BasketPage.QUANTITY_TO_ENTER)) == new_price


# 10
def test_that_final_sum_will_raise_accordingly_when_quantity_of_item_increased(self):
    self.basketPage = BasketPage(self.driver)
    self.basketPage.remove_all_good_in_basket_and_reload_page()
    self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
    for book in self.list_of_buttons_move_into_basket[0:2]:
        book.click()
    self.basketPage.do_click(TestData.CLOSE_POPUP_ANY_ACTION)
    self.basketPage.do_click(TestData.BASKET_BUTTON_AT_HEADER)
    self.list_of_quantity_of_all_items_in_basket = self.basketPage.find_several_element(
        BasketPage.QUANTITY_OF_EACH_ITEM_IN_BASKET)
    self.list_of_book_prices_in_basket = self.basketPage.find_several_element(BasketPage.BOOK_PRICE_STRING)
    price_of_first_book_string = self.list_of_book_prices_in_basket[0]
    price_of_second_book_string = self.list_of_book_prices_in_basket[1]
    first_book_price_in_basket = self.basketPage.price_by_int(price_of_first_book_string)
    second_book_price_in_basket = self.basketPage.price_by_int(price_of_second_book_string)
    first_book_input_field = self.list_of_quantity_of_all_items_in_basket[0]
    self.basketPage.clear_text_in_element_and_send_text_with_enter(
        first_book_input_field, BasketPage.QUANTITY_TO_ENTER)
    time.sleep(7)
    final_sum = self.basketPage.get_element_text(BasketPage.PURCHASE_FINAL_SUM).replace(' ', '')
    assert (first_book_price_in_basket * int(BasketPage.QUANTITY_TO_ENTER) + second_book_price_in_basket) == int(final_sum)


# 11
def test_that_start_checkout_button_open_checkout_page(self):
    self.basketPage = BasketPage(self.driver)
    self.basketPage.remove_all_good_in_basket_and_reload_page()
    self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
    self.list_of_buttons_move_into_basket[0].click()
    self.basketPage.do_click(TestData.CLOSE_POPUP_ANY_ACTION)
    self.basketPage.do_click(TestData.BASKET_BUTTON_AT_HEADER)
    self.basketPage.do_click(BasketPage.START_CHECKOUT)
    self.basketPage.is_visible(BasketPage.CHECKOUT_AND_PAY)
    current_url = self.basketPage.get_current_url()
    assert current_url == BasketPage.BASKET_URL + "checkout/"
