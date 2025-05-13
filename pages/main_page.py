import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MainPage(BasePage):
    @allure.step("Нажать кнопку 'да все привыкли'")
    def click_on_cookia_button(self):
        self.click_on_element(MainPageLocators.COOKIA_BUTTON)

    @allure.step("Кликнуть на иконку вопроса #{question_number}")
    def click_on_faq_question(self, question_number):
        self.click_on_element(MainPageLocators.faq_questions_items[question_number])

    @allure.step("Ожидание появления ответа #{question_number}")
    def wait_for_faq_answer(self, question_number):
        self.wait_for_element(MainPageLocators.faq_answers_items[question_number])

    @allure.step("Получение текста ответа #{question_number}")
    def get_faq_answer_text(self, question_number):
        return self.get_text_on_element(MainPageLocators.faq_answers_items[question_number])

    @allure.step("Нажать кнопку Заказать")
    def click_order_button(self, button_locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(button_locator)
        ).click()

    @allure.step("Нажать на логотип Самоката и проверить переход на главную страницу Самоката")
    def click_scooter_logo_and_verify(self, main_page_url):
        self.click_on_element(MainPageLocators.LOGO_SCOOTER)
        self.wait_for_url(main_page_url)
        assert self.driver.current_url == main_page_url

    @allure.step(
        "Нажать на логотип Яндекса и проверить, что в новом окне через редирект открылась главная страница Дзена")
    def click_yandex_logo_and_verify(self):
        """Проверяет переход на dzen.ru"""
        main_window = self.driver.current_window_handle
        self.click_on_element(MainPageLocators.LOGO_YANDEX)

        WebDriverWait(self.driver, 15).until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window([w for w in self.driver.window_handles if w != main_window][0])

        WebDriverWait(self.driver, 15).until(lambda d: 'dzen.ru' in d.current_url)
