import allure

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Кликаем на элемент')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Кликабельность элемента')
    def check_element_is_clickable(self, locator):
        WebDriverWait(self.driver, 8).until(
            expected_conditions.element_to_be_clickable(locator))

    @allure.step('Ожидание невидимого элемента')
    def wait_invisibility_element(self, locator):
        return WebDriverWait(self.driver, 15).until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step('Проверяем, что элемент виден')
    def check_element_is_visable(self, locator):
        WebDriverWait(self.driver, 15).until(
            expected_conditions.visibility_of_element_located(locator))

    @allure.step('Получаем текст элемента')
    def get_text_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Устанавливаем локатор')
    def set_field_by_locator(self, locator, key):
        self.driver.find_element(*locator).send_keys(key)

    @allure.step('Получаем атрибут элемента')
    def get_attribute_element(self, locator, attribute):
        return self.driver.find_element(*locator).get_attribute(attribute)

    @allure.step('Перетаскивание элемента')
    def drag_and_drop_element(self, locator_from, locator_to):
        self.check_element_is_visable(locator_from)
        self.check_element_is_visable(locator_to)
        element_from = self.driver.find_element(*locator_from)
        element_to = self.driver.find_element(*locator_to)
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
               """, element_from, element_to)