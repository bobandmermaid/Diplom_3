import allure

from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.story('Проверка основного функционала')
class TestMainFeatures:

    @allure.title('Переход по клику в Конструктор')
    def test_redirect_by_constructor_button(self, get_driver):
        constructor_page = MainPage(get_driver)
        constructor_page.click_order_feed_link()
        orders_page = OrderFeedPage(get_driver)
        orders_page.find_element_order_feed_title()
        constructor_page.click_constructor_link()
        assert constructor_page.find_element_constructor_title().is_displayed()

    @allure.title('Переход по клику в Лента заказов')
    def test_redirect_by_order_list_button(self, get_driver):
        constructor_page = MainPage(get_driver)
        constructor_page.click_order_feed_link()
        orders_page = OrderFeedPage(get_driver)
        assert orders_page.find_element_order_feed_title().is_displayed()

    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_get_ingredient_details(self, get_driver):
        constructor_page = MainPage(get_driver)
        constructor_page.click_ingredient()
        assert constructor_page.find_element_ingredient_details_title().is_displayed()

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_close_ingredient_details_window(self, get_driver):
        constructor_page = MainPage(get_driver)
        constructor_page.click_ingredient()
        constructor_page.find_element_ingredient_details_title()
        constructor_page.click_close_button()
        assert constructor_page.find_element_ingredient_details_modal()

    @allure.title('При добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_ingredient_counter_change(self, get_driver):
        constructor_page = MainPage(get_driver)
        original_number = constructor_page.get_counter_number_of_ingredient_bun()
        constructor_page.move_bun_to_cart()
        current_number = constructor_page.get_counter_number_of_ingredient_bun()
        assert int(current_number) > int(original_number)

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_successful_order(self, get_driver, login_user):
        constructor_page = MainPage(get_driver)
        constructor_page.find_element_ingredient_bun()
        constructor_page.move_bun_to_cart()
        constructor_page.move_sauce_to_cart()
        constructor_page.move_filling_to_cart()
        constructor_page.find_element_order_create_button()
        constructor_page.click_order_button()
        constructor_page.find_element_order_number_in_constructor()
        assert constructor_page.find_element_order_is_preparing_text().is_displayed()
