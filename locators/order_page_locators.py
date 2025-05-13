from selenium.webdriver.common.by import By

class OrderPageLocators:

    #Локаторы формы "Для кого самокат"

    #Поле "Имя"
    FIRST_NAME_FIELD = (By.XPATH, "//input[contains(@placeholder, '* Имя')]")
    #Поле "Фамилия"
    LAST_NAME_FIELD = (By.XPATH, "//input[contains(@placeholder, '* Фамилия')]")
    #Поле "Адрес"
    ADDRESS_FIELD = (By.XPATH, "//input[contains(@placeholder, '* Адрес')]")
    #Поле "Станция метро"
    METRO_STATION_FIELD = (By.XPATH, "//input[contains(@placeholder, '* Станция метро')]")
    #Поле "Телефон"
    PHONE_FIELD = (By.XPATH, "//input[contains(@placeholder, '* Телефон')]")
    #Кнопка "Далее" под формой "Для кого самокат"
    NEXT_BUTTON = (By.XPATH, "//button[contains(., 'Далее')]")

    #Локаторы формы "Про аренду"

    #Поле "Когда привезти самокат"
    DELIVERY_DATE_FIELD = (By.XPATH, "//input[contains(@placeholder, '* Когда')]")
    #Раскрывающийся список "Срок аренды"
    RENTAL_PERIOD_DROPDOWN = (By.CSS_SELECTOR, "div.Dropdown-control")

    #Кнопка "Заказать" под формой "Про аренду"
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM') and contains(text(), 'Заказать')]")

    #Локаторы для всплывающего окна "Хотите оформить заказ?"

    #Кнопка "Да"
    CONFIRM_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM') and contains(text(), 'Да')]")

    #Всплывающее окно "Заказ оформлен"

    #Заголовок "Заказ оформлен"
    ORDER_SUCCESS_TITLE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and text()='Заказ оформлен']")
    #Кнопка "Посмотреть статус"
    VIEW_STATUS_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM') and contains(text(), 'Посмотреть статус')]")

