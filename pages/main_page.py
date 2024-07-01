import allure

from pages.base_page import BasePage
from locators import MainLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик на кнопку Войти в аккаунт')
    def click_enter_account_button(self):
        self.move_to_element_and_press(MainLocators.ENTER_ACCOUNT_BUTTON)

    @allure.step('Клик на ингредиент')
    def click_ingredient(self):
        self.move_to_element_and_press(MainLocators.INGREDIENT_BUN)

    @allure.step('Клик на кнопку закрытия в окне ингредиента')
    def click_close_button(self):
        self.move_to_element_and_press(MainLocators.CLOSE_BUTTON)

    @allure.step('Клик на кнопку Оформить заказ')
    def click_order_button(self):
        self.move_to_element_and_press(MainLocators.ORDER_CREATE_BUTTON)

    @allure.step('Получить значение счетчика ингредиентов')
    def get_counter_number_of_ingredient_bun(self):
        return self.get_text_from_element(MainLocators.INGREDIENT_COUNTER)

    @allure.step('Перенести булку в корзину')
    def move_bun_to_cart(self):
        self.do_drag_n_drop(MainLocators.INGREDIENT_BUN, MainLocators.ORDER_CART)

    @allure.step('Перенести соус в корзину')
    def move_sauce_to_cart(self):
        self.do_drag_n_drop(MainLocators.INGREDIENT_SAUCE, MainLocators.ORDER_CART)

    @allure.step('Перенести начинку в корзину')
    def move_filling_to_cart(self):
        self.do_drag_n_drop(MainLocators.INGREDIENT_FILLING, MainLocators.ORDER_CART)

    @allure.step('Создать заказ')
    def create_order(self):
        self.find_element(MainLocators.INGREDIENT_BUN)
        self.do_drag_n_drop(MainLocators.INGREDIENT_BUN, MainLocators.ORDER_CART)
        self.do_drag_n_drop(MainLocators.INGREDIENT_FILLING, MainLocators.ORDER_CART)
        self.find_element(MainLocators.ORDER_CREATE_BUTTON)
        self.move_to_element_and_press(MainLocators.ORDER_CREATE_BUTTON)
        self.find_element(MainLocators.ORDER_IS_PREPARING_TEXT)
        self.wait_until_element_invisible(MainLocators.DEFAULT_ORDER_NUMBER)
        created_order = self.get_text_from_element(MainLocators.ORDER_NUMBER_IN_CONSTRUCTOR)
        self.move_to_element_and_press(MainLocators.CLOSE_BUTTON)
        return created_order

    def find_element_constructor_title(self):
        return self.find_element(MainLocators.CONSTRUCTOR_TITLE)

    def find_element_ingredient_details_title(self):
        return self.find_element(MainLocators.INGREDIENT_DETAILS_TITLE)

    def find_element_ingredient_details_modal(self):
        return self.wait_until_element_invisible(MainLocators.INGREDIENT_DETAILS_MODAL)

    def find_element_ingredient_bun(self):
        return self.find_element(MainLocators.INGREDIENT_BUN)

    def find_element_order_create_button(self):
        return self.find_element(MainLocators.ORDER_CREATE_BUTTON)

    def find_element_order_number_in_constructor(self):
        return self.find_element(MainLocators.ORDER_NUMBER_IN_CONSTRUCTOR)

    def find_element_order_is_preparing_text(self):
        return self.find_element(MainLocators.ORDER_IS_PREPARING_TEXT)
