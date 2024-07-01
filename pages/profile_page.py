import allure

from pages.base_page import BasePage
from locators import AccountLocators


class ProfilePage(BasePage):

    @allure.step('Клик на заголовок в Истории заказов')
    def click_history_orders_section_name(self):
        self.click_element(AccountLocators.ORDER_HISTORY_LINK)

    @allure.step('Получаем номер последнего заказа в разделе История заказов')
    def get_order_number(self):
        return self.get_text_from_element(AccountLocators.ORDER_NUMBER_IN_ORDER_HISTORY)

    @allure.step('Клик на Выход')
    def click_exit_button(self):
        self.click_element(AccountLocators.LOGOUT_BUTTON)

    def find_element_profile_link(self):
        return self.find_element(AccountLocators.PROFILE_LINK)

    def find_element_order_history_link(self):
        return self.find_element(AccountLocators.ORDER_HISTORY_LINK)

    def find_element_order_completed(self):
        return self.find_element(AccountLocators.ORDER_COMPLETED_TEXT)

    def find_element_logout_button(self):
        return self.find_element(AccountLocators.LOGOUT_BUTTON)

