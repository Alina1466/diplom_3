from selenium.webdriver.common.by import By


class ProfilePageLocators:

    LOGIN_BUTTON_PROFILE = [By.XPATH, '//button[text()= "Войти"]'] #Кнопка Войти
    RECOVERY_BUTTON_PROFILE = [By.XPATH, './/a[text()= "Восстановить пароль"]'] #Кнопка восстановить пароль
    SAVE_BTN = [By.XPATH, '//button[text()= "Сохранить"]'] #Кнопка сохранить
    EMAIL_INPUT = [By.XPATH, '//input[@name= "name"]'] #Поле ввода email
    PASSWORD_INPUT = [By.XPATH, '//input[@name= "Пароль"]'] #Поле ввода пароля
    HISTORY_BTN = [By.XPATH, './/a[@href= "/account/order-history"]'] #Кнопка истории
    EXIT_BTN = [By.XPATH, '//button[text()="Выход"]'] #Кнопка Выйти
    HISTORY_LIST_PROFILE = [By.XPATH, ".//div[contains(@class,'OrderHistory_textBox')]/p[contains(@class,'text_type_digits')]"]
