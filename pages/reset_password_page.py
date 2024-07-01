import allure
from pages.base_page import BasePage
from locators.reset_password_locators import ResetPasswordLocators


class ResetPasswordPage(BasePage):

    @allure.step('Проверяем видимость кнопки "Сохранить"')
    def check_btn_save_is_visible(self):
        self.check_element_is_visable(ResetPasswordLocators.BTN_SAVE)

    @allure.step('Получаем текст кнопки "Сохранить"')
    def get_text_btn_save(self):
        return self.get_text_element(ResetPasswordLocators.BTN_SAVE)

    @allure.step('Кликаем по кнопке "показать/скрыть пароль"')
    def click_on_eye_btn(self):
        self.click_on_element(ResetPasswordLocators.BTN_EYE)

    @allure.step('Получить значение атрибута поля ввода email')
    def get_attribute_email_input(self):
        return self.get_attribute_element(ResetPasswordLocators.EMAIL, 'type')