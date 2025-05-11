from selenium.webdriver.common.by import By

class MainPageLocators:

    #Верхняя кнопка "Заказать"
    ORDER_BUTTON_TOP = (By.XPATH, "//button[contains(@class, 'Button_Button') and contains(text(), 'Заказать')][1]")
    #Нижняя кнопка "Заказать"
    ORDER_BUTTON_BUTTOM = (By.XPATH,
                           "(//button[contains(@class, 'Button_Button') and contains(text(), 'Заказать')])[2]")

    #Кнопка Cookia (да все привыкли)
    COOKIA_BUTTON = (By.ID, "rcc-confirm-button")

    #Список с вопросами
    faq_questions_items = {
        0: (By.ID, "accordion__heading-0"),
        1: (By.ID, "accordion__heading-1"),
        2: (By.ID, "accordion__heading-2"),
        3: (By.ID, "accordion__heading-3"),
        4: (By.ID, "accordion__heading-4"),
        5: (By.ID, "accordion__heading-5"),
        6: (By.ID, "accordion__heading-6"),
        7: (By.ID, "accordion__heading-7"),
    }

    #Список с ответами
    faq_answers_items = {
        0: (By.ID, "accordion__panel-0"),
        1: (By.ID, "accordion__panel-1"),
        2: (By.ID, "accordion__panel-2"),
        3: (By.ID, "accordion__panel-3"),
        4: (By.ID, "accordion__panel-4"),
        5: (By.ID, "accordion__panel-5"),
        6: (By.ID, "accordion__panel-6"),
        7: (By.ID, "accordion__panel-7")
    }