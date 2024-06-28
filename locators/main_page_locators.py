from selenium.webdriver.common.by import By


class MainPageLocators:

    LOGIN_MAIN_BUTTON = [By.XPATH, './/button[text()= "Войти в аккаунт"]']
    PROFILE_BUTTON = [By.XPATH, './/a[@href= "/account"]']
    ORDER_MAIN_BTN = [By.XPATH, './/button[text()= "Оформить заказ"]']
    DONE_TITLE = [By.XPATH, "//p[text()='Готовы:']"]
    BUN_01 = [By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']"]
    H2_POPUP = [By.XPATH, '//h2[contains(@class, "Modal_modal__title_modified__3Hjkd")]']
    X_POPUP_BTN = [By.XPATH, '//h2[contains(@class, "Modal_modal__title_modified__3Hjkd")]']
    X_POPUP_BTN_OFFER = [By.XPATH, '//button[contains(@class, "Modal_modal__close_modified__3V5XS")]']
    SAUCE_02 = [By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa72"]']
    BUN_1 = [By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6d]']
    BURGER_DROP_PLACE = [By.XPATH, "//ul[@class='BurgerConstructor_basket__list__l9dp_']"]
    COUNTER_SAUCE = [By.XPATH, "//img[@alt='Соус Spicy-X']/parent::*//p[@class='counter_counter__num__3nue1']"]
    START_ORDER_TITLE = [By.XPATH, './/p[text()= "идентификатор заказа"]']
    ORDER_LIST_ALL = [By.XPATH, ".//div[contains(@class,'OrderHistory_textBox')]/p[contains(@class,'text_type_digits')]"]
    ORDER_STATUS_TEXT = [By.XPATH, '//p[text()="Ваш заказ начали готовить"]']
    DEFAULT_ORDER_NUMBER = [By.XPATH, '//h2[text()="9999"]']
    CURRENT_ORDER_NUMBER = [By.XPATH, '//*[contains(@class, "type_digits-large")]']