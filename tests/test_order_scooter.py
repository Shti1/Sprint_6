import allure
import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import Data
from locators.main_page_locators import MainPageLocators


@allure.feature("Заказ самоката")
class TestOrderScooter:
    @pytest.mark.parametrize("button_locator,button_name", [
        (MainPageLocators.ORDER_BUTTON_TOP, "верхнюю кнопку 'Заказать'"),
        (MainPageLocators.ORDER_BUTTON_BUTTOM, "нижнюю кнопку 'Заказать'")
    ], ids=["top_button", "bottom_button"])
    @allure.title("Проверка оформления заказа через {button_name}")
    def test_order_via_different_entries(self, driver, button_locator, button_name):
        with allure.step("Инициализация страниц"):
            main_page = MainPage(driver)
            order_page = OrderPage(driver)
            user_data = Data.get_test_user()

        with allure.step("1. Принимаем куки"):
            main_page.click_on_cookia_button()

        with allure.step(f"2. Нажимаем {button_name}"):
            main_page.click_order_button(button_locator)

        with allure.step("3. Заполняем форму 'Для кого самокат'"):
            order_page.fill_recipient_form(user_data)

        with allure.step("4. Нажимаем кнопку 'Далее'"):
            order_page.click_next_button()

        with allure.step("5. Заполняем форму 'Про аренду'"):
            order_page.fill_rental_details(user_data)

        with allure.step("6. Нажимаем кнопку 'Заказать'"):
            order_page.click_order_button()

        with allure.step("7. Нажимаем кнопку 'Да'"):
            order_page.click_confirm_button()

        with allure.step("8. Проверить подтверждение заказа"):
            assert order_page.verify_order_confirmation()
