import allure
from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators


class ProfilePage(BasePage):

    @allure.step('Проверяем видимость кнопки логина')
    def check_button_login_is_visible(self):
        self.check_element_is_visable(ProfilePageLocators.LOGIN_BUTTON_PROFILE)

    @allure.step('Получаем текст кнопки логина')
    def get_text_login_button(self):
        return self.get_text_element(ProfilePageLocators.LOGIN_BUTTON_PROFILE)

    @allure.step('Кликаем на кнопку войти')
    def click_on_login_btn(self):
        self.click_on_element(ProfilePageLocators.LOGIN_BUTTON_PROFILE)

    @allure.step('Проверяем  кликабильность кнопки восстановления')
    def check_recovery_button_profile_is_clickable(self):
        self.check_element_is_clickable(ProfilePageLocators.RECOVERY_BUTTON_PROFILE)

    @allure.step('Кликаем по кнопке "Восстановить пароль"')
    def click_on_recovery_button_profile(self):
        self.click_on_element(ProfilePageLocators.RECOVERY_BUTTON_PROFILE)

    @allure.step('Проверяем видимость кнопки сохранения информации профиля')
    def check_btn_save_is_visible(self):
        self.check_element_is_visable(ProfilePageLocators.SAVE_BTN)

    @allure.step('Кликаем по кнопке "Сохранить"')
    def click_on_save_btn_profile(self):
        self.click_on_element(ProfilePageLocators.SAVE_BTN)

    @allure.step('Получаем текст кнопки "Сохранить"')
    def get_text_save_btn(self):
        return self.get_text_element(ProfilePageLocators.SAVE_BTN)

    @allure.step('Вводим данные почты')
    def set_email(self, email):
        self.set_field_by_locator(ProfilePageLocators.EMAIL_INPUT, email)

    @allure.step('Вводим пароль')
    def set_password(self, password):
        self.set_field_by_locator(ProfilePageLocators.PASSWORD_INPUT, password)

    @allure.step('Кликаем по кнопке "История заказов"')
    def click_on_history_btn_profile(self):
        self.click_on_element(ProfilePageLocators.HISTORY_BTN)

    @allure.step('Получить значение атрибута кнопки')
    def get_attribute_history_btn(self):
        return self.get_attribute_element(ProfilePageLocators.HISTORY_BTN, 'aria-current')

    @allure.step('Кликаем по кнопке "Выхода"')
    def click_on_exit_btn_profile(self):
        self.click_on_element(ProfilePageLocators.EXIT_BTN)

    @allure.step('Проверяем  кликабильность кнопки выхода')
    def check_exit_btn_is_clickable(self):
        self.check_element_is_clickable(ProfilePageLocators.EXIT_BTN)

    @allure.step('Ждем пока загрузится история заказов пользователя')
    def check_orders_history_profile_is_visible(self):
        self.check_element_is_visable(ProfilePageLocators.HISTORY_LIST_PROFILE)

    @allure.step('Получаем список заказов пользователя')
    def get_list_orders_user(self):
        list_orders = []
        for lo in self.get_find_element(*ProfilePageLocators.HISTORY_LIST_PROFILE):
            list_orders.append(lo.text)
        return list_orders