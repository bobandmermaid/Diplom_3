import allure

from pages.order_feed_page import OrderFeedPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from locators import OrderFeedLocators, MainLocators, AccountLocators


@allure.story('Проверка раздела Лента заказов')
class TestOrderFeed:

    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_press_order_get_popup(self, get_driver):
        main_page = MainPage(get_driver)
        main_page.click_order_feed_link()
        orders_page = OrderFeedPage(get_driver)
        orders_page.find_element(OrderFeedLocators.ORDER_FEED_TITLE)
        orders_page.click_order()
        assert orders_page.find_element(OrderFeedLocators.ORDER_CONTENTS_TITLE).is_displayed()

    @allure.title('Заказы пользователя из раздела История заказов отображаются на странице Лента заказов')
    def test_user_order_displayed_in_feed(self, get_driver, login_user, create_order):
        main_page = MainPage(get_driver)
        main_page.find_element(MainLocators.CONSTRUCTOR_TITLE)
        main_page.click_account_link()
        account_page = ProfilePage(get_driver)
        account_page.find_element(AccountLocators.ORDER_HISTORY_LINK)
        account_page.click_history_orders_section_name()
        account_page.find_element(AccountLocators.ORDER_COMPLETED_TEXT)
        user_order = account_page.get_order_number()
        account_page.click_order_feed_link()
        orders_page = OrderFeedPage(get_driver)
        orders_page.find_element(OrderFeedLocators.ORDER_FEED_TITLE)
        assert orders_page.find_order_in_order_list(user_order).is_displayed()

    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_increment_total_orders_counter(self, get_driver, login_user):
        main_page = MainPage(get_driver)
        main_page.find_element(MainLocators.CONSTRUCTOR_TITLE)
        main_page.click_order_feed_link()
        orders_page = OrderFeedPage(get_driver)
        orders_page.find_element(OrderFeedLocators.ORDER_FEED_TITLE)
        total_orders_count = orders_page.get_total_orders_number()
        orders_page.click_constructor_link()
        main_page.find_element(MainLocators.CONSTRUCTOR_TITLE)
        main_page.create_order()
        orders_page.click_order_feed_link()
        orders_page.find_element(OrderFeedLocators.ORDER_FEED_TITLE)
        assert int(orders_page.get_total_orders_number()) == (int(total_orders_count) + 1)

    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_increment_today_orders_counter(self, get_driver, login_user):
        main_page = MainPage(get_driver)
        main_page.find_element(MainLocators.CONSTRUCTOR_TITLE)
        main_page.click_order_feed_link()
        orders_page = OrderFeedPage(get_driver)
        orders_page.find_element(OrderFeedLocators.ORDER_FEED_TITLE)
        today_orders_count = orders_page.get_today_orders_number()
        orders_page.click_constructor_link()
        main_page.find_element(MainLocators.CONSTRUCTOR_TITLE)
        main_page.create_order()
        main_page.click_order_feed_link()
        orders_page.find_element(OrderFeedLocators.ORDER_FEED_TITLE)
        assert int(orders_page.get_today_orders_number()) == (int(today_orders_count) + 1)

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    def test_create_order_get_number_in_work_list(self, get_driver, login_user):
        main_page = MainPage(get_driver)
        main_page.find_element(MainLocators.CONSTRUCTOR_TITLE)
        created_order = main_page.create_order()
        main_page.click_order_feed_link()
        orders_page = OrderFeedPage(get_driver)
        orders_page.find_element(OrderFeedLocators.ORDER_NUMBER_IN_WORK)
        assert int(orders_page.get_order_number_in_work_list()) == int(created_order)
