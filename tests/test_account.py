import allure

from pages.profile_page import ProfilePage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from locators import MainLocators, LoginLocators, AccountLocators


@allure.story('Проверка Личного кабинета')
class TestAccountPage:

    @allure.title('Переход по клику на Личный кабинет')
    def test_account_link_redirect(self, get_driver, login_user):
        constructor_page = MainPage(get_driver)
        constructor_page.find_element(MainLocators.CONSTRUCTOR_TITLE)
        constructor_page.click_account_link()
        account_page = ProfilePage(get_driver)
        assert account_page.find_element(AccountLocators.PROFILE_LINK).is_displayed()

    @allure.title('Переход в раздел История заказов')
    def test_redirect_to_order_history(self, get_driver, login_user, create_order):
        constructor_page = MainPage(get_driver)
        constructor_page.find_element(MainLocators.CONSTRUCTOR_TITLE)
        constructor_page.click_account_link()
        account_page = ProfilePage(get_driver)
        account_page.find_element(AccountLocators.ORDER_HISTORY_LINK)
        account_page.click_history_orders_section_name()
        assert account_page.find_element(AccountLocators.ORDER_COMPLETED_TEXT).is_displayed()

    @allure.title('Выход из аккаунта')
    def test_account_logout_via_button(self, get_driver, login_user):
        constructor_page = MainPage(get_driver)
        constructor_page.find_element(MainLocators.CONSTRUCTOR_TITLE)
        constructor_page.click_account_link()
        account_page = ProfilePage(get_driver)
        account_page.find_element(AccountLocators.LOGOUT_BUTTON)
        account_page.click_exit_button()
        login_page = LoginPage(get_driver)
        assert login_page.find_element(LoginLocators.ENTER_BUTTON).is_displayed()
