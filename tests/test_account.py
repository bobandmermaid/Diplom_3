import allure

from pages.profile_page import ProfilePage
from pages.login_page import LoginPage
from pages.main_page import MainPage


@allure.story('Проверка Личного кабинета')
class TestAccountPage:

    @allure.title('Переход по клику на Личный кабинет')
    def test_account_link_redirect(self, get_driver, login_user):
        constructor_page = MainPage(get_driver)
        constructor_page.find_element_constructor_title()
        constructor_page.click_account_link()
        account_page = ProfilePage(get_driver)
        assert account_page.find_element_profile_link().is_displayed()

    @allure.title('Переход в раздел История заказов')
    def test_redirect_to_order_history(self, get_driver, login_user, create_order):
        constructor_page = MainPage(get_driver)
        constructor_page.find_element_constructor_title()
        constructor_page.click_account_link()
        account_page = ProfilePage(get_driver)
        account_page.find_element_order_history_link()
        account_page.click_history_orders_section_name()
        assert account_page.find_element_order_completed().is_displayed()

    @allure.title('Выход из аккаунта')
    def test_account_logout_via_button(self, get_driver, login_user):
        constructor_page = MainPage(get_driver)
        constructor_page.find_element_constructor_title()
        constructor_page.click_account_link()
        account_page = ProfilePage(get_driver)
        account_page.find_element_logout_button()
        account_page.click_exit_button()
        login_page = LoginPage(get_driver)
        assert login_page.find_element_enter_button().is_displayed()
