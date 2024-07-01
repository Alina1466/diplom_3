from selenium.webdriver.common.by import By


class RecoveryPageLocators:

    RECOVERY_BUTTON = [By.XPATH, '//button[text()= "Восстановить"]'] #Кнопка восстановить пароль
    EMAIL = [By.XPATH, '//input[@name="name"]'] #Поле email