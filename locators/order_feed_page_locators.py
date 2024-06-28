from selenium.webdriver.common.by import By


class OrderPageLocators:
    FIRST_ORDER_IN_LIST = [By.XPATH, './/li[contains(@class,"OrderHistory_listItem__2x95r")][1]']
    ORDER_IS_DONE_TITLE = [By.XPATH, './/p[text()= "Выполнен"]']
    X_FEED_POPUP_BTN = [By.XPATH, '//button[contains(@class, "Modal_modal__close_modified__3V5XS")]']
    POPUP_ORDER_WINDOW = [By.XPATH, ".//div[contains(@class,'Modal_orderBox')]/p"]
    ALL_TIME_COUNTER_VALUE = [By.XPATH, ".//p[text()='Выполнено за все время:']/../p[contains(@class,'OrderFeed_number')]"]
    TODAY_COUNTER_VALUE = [By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class,"digits-large")]']
    ORDER_IN_WORK = [By.XPATH, '//*[contains(@class,"orderListReady")]//li[contains(@class,"digits-default")]']
