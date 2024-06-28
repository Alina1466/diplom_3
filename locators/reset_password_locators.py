from selenium.webdriver.common.by import By


class ResetPasswordLocators:

    EMAIL = [By.XPATH, '//input[@name="Введите новый пароль"]']  # Поле ввода пароля
    BTN_SAVE = [By.XPATH, './/button[text()= "Сохранить"]']
    BTN_EYE = [By.CLASS_NAME, 'input__icon']