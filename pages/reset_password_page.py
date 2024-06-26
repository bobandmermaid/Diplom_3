import allure

from pages.base_page import BasePage
from locators import BaseLocators, ResetPasswordLocators


class ResetPasswordPage(BasePage):

    @allure.step("Ввод почты")
    def fill_email(self, email):
        self.fill_field(BaseLocators.EMAIL_FIELD, email)

    @allure.step("Клик по кнопке «Восстановить»")
    def click_reset_pass_button(self):
        self.click_element(ResetPasswordLocators.RESET_BUTTON)

    @allure.step("Клик по кнопке показать/скрыть пароль")
    def click_show_password_icon(self):
        self.move_to_element_and_press(ResetPasswordLocators.SHOW_PASSWORD_ICON)
