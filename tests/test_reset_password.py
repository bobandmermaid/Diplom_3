import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.reset_password_page import ResetPasswordPage


@allure.story('Проверка восстановления пароля')
class TestResetPassword:

    @allure.title('Переход на страницу восстановления пароля по кнопке Восстановить пароль')
    def test_reset_link_redirects_to_reset_page(self, get_driver):
        constructor_page = MainPage(get_driver)
        constructor_page.click_enter_account_button()
        login_page = LoginPage(get_driver)
        login_page.click_reset_password()
        reset_pass_page = ResetPasswordPage(get_driver)
        assert reset_pass_page.find_element_reset_button().is_displayed()

    @allure.title('Ввод почты и клик по кнопке Восстановить')
    def test_fill_email_press_reset_button(self, get_driver, gen_email):
        constructor_page = MainPage(get_driver)
        constructor_page.click_enter_account_button()
        login_page = LoginPage(get_driver)
        login_page.click_reset_password()
        reset_pass_page = ResetPasswordPage(get_driver)
        reset_pass_page.fill_email(gen_email)
        reset_pass_page.click_reset_pass_button()
        assert reset_pass_page.find_element_save_button().is_displayed()

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_show_pass_makes_field_active(self, get_driver, gen_email):
        constructor_page = MainPage(get_driver)
        constructor_page.click_enter_account_button()
        login_page = LoginPage(get_driver)
        login_page.click_reset_password()
        reset_pass_page = ResetPasswordPage(get_driver)
        reset_pass_page.fill_email(gen_email)
        reset_pass_page.click_reset_pass_button()
        reset_pass_page.find_element_save_button()
        reset_pass_page.click_show_password_icon()
        assert reset_pass_page.find_element_password_field_active().is_displayed()
