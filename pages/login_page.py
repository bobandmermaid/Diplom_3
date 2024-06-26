import allure

from pages.base_page import BasePage
from locators import BaseLocators, LoginLocators


class LoginPage(BasePage):

    @allure.step('Кликнуть кнопку Восстановить пароль')
    def click_reset_password(self):
        self.click_element(LoginLocators.FORGOT_PASSWORD_LINK)

    @allure.step('Кликнуть на кнопку Войти')
    def click_enter_button(self):
        self.click_element(LoginLocators.ENTER_BUTTON)

    @allure.step('Ввести email на странице Вход')
    def fill_email_field(self, email):
        self.fill_field(BaseLocators.EMAIL_FIELD, email)

    @allure.step('Ввести пароль на странице Вход')
    def fill_password_field(self, password):
        self.fill_field(BaseLocators.PASSWORD_FIELD, password)
