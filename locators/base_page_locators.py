from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGO = [By.XPATH, '//div[@class= "AppHeader_header__logo__2D0X2"]/a']
    MAIN_TITLE = [By.XPATH, "//h1"]
    CONSTRUCTOR_BTN = [By.XPATH, "//p[text()='Конструктор']"]
    ORDER_FEED_BTN = [By.XPATH, "//p[text()='Лента Заказов']"]