from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.by import By


class OrderPage(BasePage):

    @allure.step("Заполнить форму Для кого самокат")
    def fill_recipient_form(self, user_data):
        """Заполняет форму данными пользователя"""
        # Заполнение текстовых полей
        self.send_keys_to_input(OrderPageLocators.FIRST_NAME_FIELD, user_data['first_name'])
        self.send_keys_to_input(OrderPageLocators.LAST_NAME_FIELD, user_data['last_name'])
        self.send_keys_to_input(OrderPageLocators.ADDRESS_FIELD, user_data['address'])

        # Выбор станции метро
        metro_field = self.wait_for_element(OrderPageLocators.METRO_STATION_FIELD)
        metro_field.click()
        metro_field.send_keys(user_data['metro'] + Keys.DOWN + Keys.ENTER)

        # Заполнение телефона
        self.send_keys_to_input(OrderPageLocators.PHONE_FIELD, user_data['phone'])

    @allure.step("Нажать на кнопку Далее")
    def click_next_button(self):
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить форму Про аренду")
    def fill_rental_details(self, user_data):
        # 1. Заполняем дату доставки
        self.send_keys_to_input(OrderPageLocators.DELIVERY_DATE_FIELD, user_data['delivery_date'])

        # 2. Закрываем календарь даты (если открыт)
        self.driver.find_element(*OrderPageLocators.DELIVERY_DATE_FIELD).send_keys(Keys.ESCAPE)

        # 3. Работаем с выпадающим списком срока аренды
        # 3.1. Прокручиваем и кликаем dropdown
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)

        # 3.2. Кликаем для открытия списка
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        ).click()

        # 3.3. Выбираем случайный период из data.py
        period = user_data['rental_period']
        option_locator = (By.XPATH, f"//div[@class='Dropdown-option' and text()='{period}']")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(option_locator)
        ).click()

    @allure.step("Нажать на кнопку Заказать")
    def click_order_button(self):
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтвердить оформление заказа")
    def click_confirm_button(self):
        self.click_on_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Проверить подтверждение заказа")
    def verify_order_confirmation(self):
        confirmation_element = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(OrderPageLocators.ORDER_SUCCESS_TITLE)
        )
        actual_text = confirmation_element.text
        return "Заказ оформлен" in actual_text and "Номер заказа" in actual_text

    @allure.step("Нажать на кнопку Посмотреть статус")
    def click_view_status_button(self):
        self.click_on_element(OrderPageLocators.VIEW_STATUS_BUTTON)

    @allure.step("Нажать на логотип Самоката и проверить переход на главную страницу Самоката")
    def click_scooter_logo_and_verify(self, main_page_url):
        self.click_on_element(OrderPageLocators.LOGO_SCOOTER)
        self.wait_for_url(main_page_url)
        assert self.driver.current_url == main_page_url

    @allure.step("Нажать на логотип Яндекса и проверить, что в новом окне через редирект открылась главная страница Дзена")
    def click_yandex_logo_and_verify(self):
        """Проверяет переход на dzen.ru"""
        main_window = self.driver.current_window_handle
        self.click_on_element(OrderPageLocators.LOGO_YANDEX)

        WebDriverWait(self.driver, 15).until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window([w for w in self.driver.window_handles if w != main_window][0])

        WebDriverWait(self.driver, 15).until(lambda d: 'dzen.ru' in d.current_url)


