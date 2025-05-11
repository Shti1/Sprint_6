import allure
import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import Data
from curl import main_site
from locators.main_page_locators import MainPageLocators


@allure.feature("Заказ самоката")
class TestOrderScooter:
    @pytest.mark.parametrize("button_locator", [
        MainPageLocators.ORDER_BUTTON_TOP,
        MainPageLocators.ORDER_BUTTON_BUTTOM
    ], ids=["top_botton", "bottom_button"])
    @allure.title("Заказ через разные точки входа 'Заказать'")
    def test_order_via_different_entries(self, driver, button_locator):
        with allure.step("Инициализация страниц"):
            main_page = MainPage(driver)
            order_page = OrderPage(driver)
            user_data = Data.get_test_user()

        with allure.step("1. Нажимаем кнопку 'да все привыкли'"):
            main_page.click_on_cookia_button()

        button_info = {
            MainPageLocators.ORDER_BUTTON_TOP: "Верхняя кнопка 'Заказать'",
            MainPageLocators.ORDER_BUTTON_BUTTOM: "Нижняя кнопка 'Заказать'"
        }

        with allure.step(f"2. Нажимаем {button_info[button_locator]}"):
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

        with allure.step("9. Нажимаем кнопку 'Посмотреть статус'"):
            order_page.click_view_status_button()

        with allure.step("10. Нажимаем на логотип Самоката и проверяем переход на главную страницу Самоката"):
            order_page.click_scooter_logo_and_verify(main_site)

        with allure.step("11. Нажать на логотип Яндекса и проверить, что в новом окне через редирект открылась главная страница Дзена"):
            order_page.click_yandex_logo_and_verify()
