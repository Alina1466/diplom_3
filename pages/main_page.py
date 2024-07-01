import allure
from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Проверяем, что кнопка личного кабинета доступна для клика')
    def check_button_profile_is_clickable(self):
        self.check_element_is_clickable(MainPageLocators.PROFILE_BUTTON)

    @allure.step('Кликаем по кнопке "Личный кабинет"')
    def click_on_profile_button(self):
        self.click_on_element(MainPageLocators.PROFILE_BUTTON)

    @allure.step('Кликаем по кнопке "Конструктор"')
    def click_on_constructor_button(self):
        self.click_on_element(BasePageLocators.CONSTRUCTOR_BTN)

    @allure.step('Получаем текст заголовка')
    def get_text_title(self):
        return self.get_text_element(BasePageLocators.MAIN_TITLE)

    @allure.step('Ожидаем видимость кнопки "Оформить заказ"')
    def check_order_btn_is_visible(self):
        self.check_element_is_visable(MainPageLocators.ORDER_MAIN_BTN)

    @allure.step('Кликаем на кнопку "Оформить заказ"')
    def click_on_order_btn(self):
        self.click_on_element(MainPageLocators.ORDER_MAIN_BTN)

    @allure.step('Ожидаем видимость кнопки "Войти в аккаунт"')
    def check_login_main_btn_is_visible(self):
        self.check_element_is_visable(MainPageLocators.LOGIN_MAIN_BUTTON)

    @allure.step('Ожидаем кликабельность кнопки "Войти в аккаунт"')
    def check_login_main_btn_is_clickable(self):
        self.check_element_is_clickable(MainPageLocators.LOGIN_MAIN_BUTTON)

    @allure.step('Ожидаем кликабельность кнопки "Лента заказов"')
    def check_order_feed_btn_is_clickable(self):
        self.check_element_is_clickable(BasePageLocators.ORDER_FEED_BTN)

    @allure.step('Кликаем по кнопке "Лента заказов"')
    def click_on_order_feed_button(self):
        self.click_on_element(BasePageLocators.ORDER_FEED_BTN)

    @allure.step('Ожидаем видимость кнопки "Войти в аккаунт"')
    def check_done_title_is_visible(self):
        self.check_element_is_visable(MainPageLocators.DONE_TITLE)

    @allure.step('Ожидаем видимость первого ингредиента')
    def check_first_ingredient_is_visible(self):
        self.check_element_is_visable(MainPageLocators.BUN_01)

    @allure.step('Кликаем по первому ингредиенту')
    def click_on_first_ingredient(self):
        self.click_on_element(MainPageLocators.BUN_01)

    @allure.step('Ожидаем видимость заголовка в попапе')
    def check_popup_title_is_visible(self):
        self.check_element_is_visable(MainPageLocators.H2_POPUP)

    @allure.step('Получаем текст заголовка в попапе')
    def get_text_title_popup(self):
        return self.get_text_element(MainPageLocators.H2_POPUP)

    @allure.step('Кликаем по крестику в попапе')
    def click_on_close_popup_btn(self):
        self.click_on_element(MainPageLocators.X_POPUP_BTN)

    @allure.step('Добавление начинки в корзину')
    def add_filling_to_order_basket(self):
        self.drag_and_drop_element(MainPageLocators.SAUCE_02, MainPageLocators.BURGER_DROP_PLACE)

    @allure.step('Добавление булки в корзину')
    def add_bun_to_order_basket(self):
        self.drag_and_drop_element(MainPageLocators.BUN_01, MainPageLocators.BURGER_DROP_PLACE)

    @allure.step('Получаем текст счетчика ингредиента')
    def get_counter_sauce(self):
        return self.get_text_element(MainPageLocators.COUNTER_SAUCE)

    @allure.step('Ожидаем видимость заголовка что заказ начали готовить')
    def check_start_order_title_is_visible(self):
        self.check_element_is_visable(MainPageLocators.START_ORDER_TITLE)

    @allure.step('Получаем текст заголовка что заказ начали готовить')
    def get_text_start_order_title(self):
        return self.get_text_element(MainPageLocators.START_ORDER_TITLE)

    @allure.step('Получаем номера заказов из "Ленты заказов"')
    def get_list_orders(self):
        list_orders = []
        for i in self.get_find_element(*MainPageLocators.ORDER_LIST_ALL):
            list_orders.append(i.text)
        return list_orders

    @allure.step('Ждем кликабельности кнопки закрытияч попапа')
    def check_x_btn_order_popup_is_clickable(self):
        self.check_element_is_clickable(MainPageLocators.X_POPUP_BTN_OFFER)

    @allure.step('Кликаем по кнопке крестика после оформления заказа')
    def click_on_x_btn_order_popup(self):
        self.click_on_element(MainPageLocators.X_POPUP_BTN_OFFER)

    @allure.step('Ждем пока будет видно заголовок')
    def check_order_status_text_is_visible(self):
        self.check_element_is_visable(MainPageLocators.ORDER_STATUS_TEXT)

    @allure.step('Ждем пока невидимый заголовок будет видно')
    def check_order_default_status_text_is_visible(self):
        self.wait_invisibility_element(MainPageLocators.DEFAULT_ORDER_NUMBER)

    @allure.step('Получение номера заказа')
    def get_order_number(self):
        self.get_text_element(MainPageLocators.CURRENT_ORDER_NUMBER)