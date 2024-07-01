import allure

from pages.base_page import BasePage
from locators import ResetPasswordLocators


class ResetPasswordPage(BasePage):

    @allure.step("Ввод почты")
    def fill_email(self, email):
        self.fill_field(ResetPasswordLocators.EMAIL_FIELD, email)

    @allure.step("Клик по кнопке «Восстановить»")
    def click_reset_pass_button(self):
        self.click_element(ResetPasswordLocators.RESET_BUTTON)

    @allure.step("Клик по кнопке показать/скрыть пароль")
    def click_show_password_icon(self):
        self.move_to_element_and_press(ResetPasswordLocators.SHOW_PASSWORD_ICON)

    def find_element_reset_button(self):
        return self.find_element(ResetPasswordLocators.RESET_BUTTON)

    def find_element_save_button(self):
        return self.find_element(ResetPasswordLocators.SAVE_BUTTON)

    def find_element_password_field_active(self):
        return self.find_element(ResetPasswordLocators.PASSWORD_FIELD_ACTIVE)
