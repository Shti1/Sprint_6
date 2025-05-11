import allure
import pytest

from data import Data
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators

class TestFaqSection:
    @allure.title("Проверка текста при раскрытии вопросов в FAQ")
    @pytest.mark.parametrize("question_number, expected_text", Data.faq_answers)
    def test_faq_answers(self, driver, question_number, expected_text):
        # Arrange
        main_page = MainPage(driver)
        main_page.scroll_to_element(MainPageLocators.faq_questions_items[question_number])
        # Act
        main_page.click_on_cookia_button()
        main_page.click_on_faq_question(question_number)
        main_page.wait_for_faq_answer(question_number)
        actual_text = main_page.get_faq_answer_text(question_number)
        # Assert
        assert actual_text == expected_text