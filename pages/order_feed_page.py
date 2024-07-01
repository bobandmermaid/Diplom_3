import allure

from pages.base_page import BasePage
from locators import OrderFeedLocators


class OrderFeedPage(BasePage):

    @allure.step('Кликнуть на заказ')
    def click_order(self):
        self.click_element(OrderFeedLocators.ORDER_IN_FEED_LINK)

    @allure.step('Найти заказ')
    def find_order_in_order_list(self, chosen_order):
        method, locator = OrderFeedLocators.ORDER_NUMBER_IN_ORDER_FEED
        locator = locator.format(chosen_order)
        return self.find_element((method, locator))

    @allure.step('Получить значение счетчика Выполнено за всё время')
    def get_total_orders_number(self):
        return self.get_text_from_element(OrderFeedLocators.COMPLETE_ORDERS_COUNT_TOTAL)

    @allure.step('Получить значение счетчика Выполнено за сегодня')
    def get_today_orders_number(self):
        return self.get_text_from_element(OrderFeedLocators.COMPLETE_ORDERS_COUNT_TODAY)

    @allure.step('Получить значение счетчика В работе')
    def get_order_number_in_work_list(self):
        return self.get_text_from_element(OrderFeedLocators.ORDER_NUMBER_IN_WORK)

    def find_element_order_feed_title(self):
        return self.find_element(OrderFeedLocators.ORDER_FEED_TITLE)

    def find_element_order_contents_title(self):
        return self.find_element(OrderFeedLocators.ORDER_CONTENTS_TITLE)

    def find_element_order_number_in_work(self):
        return self.get_text_from_element(OrderFeedLocators.ORDER_NUMBER_IN_WORK)
