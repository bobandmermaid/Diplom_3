import allure

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.ui import WebDriverWait
from locators import BaseLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step('Найти элемент')
    def find_element(self, locator):
        return self.wait.until(expected.visibility_of_element_located(locator))

    @allure.step('Кликнуть по элементу, когда он станет видимым')
    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    @allure.step('Ожидать, пока элемент исчезнет')
    def wait_until_element_invisible(self, locator):
        return self.wait.until(expected.invisibility_of_element_located(locator))

    @allure.step('Получить текст из элемента')
    def get_text_from_element(self, locator):
        return self.find_element(locator).text

    @allure.step('Заполнить поле')
    def fill_field(self, locator, value):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(value)

    @allure.step('Переместиться до элемента и нажать его')
    def move_to_element_and_press(self, locator):
        element = self.find_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    @allure.step('Переместить элемент к другому')
    def do_drag_n_drop(self, source_locator, target_locator):
        source_element = self.find_element(source_locator)
        target_element = self.find_element(target_locator)
        self.driver.execute_script("""
                    var source = arguments[0];
                    var target = arguments[1];
                    var evt = document.createEvent("DragEvent");
                    evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                    source.dispatchEvent(evt);
                    evt = document.createEvent("DragEvent");
                    evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                    target.dispatchEvent(evt);
                    evt = document.createEvent("DragEvent");
                    evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                    target.dispatchEvent(evt);
                    evt = document.createEvent("DragEvent");
                    evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                    target.dispatchEvent(evt);
                    evt = document.createEvent("DragEvent");
                    evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                    source.dispatchEvent(evt);
                """, source_element, target_element)

    @allure.step('Клик в хэдере на ссылку Конструктор')
    def click_constructor_link(self):
        self.click_element(BaseLocators.CONSTRUCTOR_LINK)

    @allure.step('Клик в хэдере нп ссылку Лента заказов')
    def click_order_feed_link(self):
        self.move_to_element_and_press(BaseLocators.ORDER_FEED_LINK)

    @allure.step('Клик в хэдере на ссылку Личный кабинет')
    def click_account_link(self):
        self.move_to_element_and_press(BaseLocators.ACCOUNT_LINK)
