import allure
import pytest

from pages.main_page import MainPage
from curl import main_site


@allure.feature("Заказ самоката")
class TestLogoRedirect:
    @allure.title("Проверка перехода на главную по логотипу Самоката")
    def test_scooter_logo_redirect(self, driver):
        """Проверка редиректа по логотипу Самоката"""
        with allure.step("Инициализация страниц"):
            main_page = MainPage(driver)

        with allure.step("1. Принимаем куки'"):
            main_page.click_on_cookia_button()

        with allure.step("2. Нажимаем на логотип Самоката и проверяем переход на главную страницу Самоката"):
            main_page.click_scooter_logo_and_verify(main_site)

    @allure.title("Проверка перехода на Дзен по логотипу Яндекса")
    def test_yandex_logo_redirect(self, driver):
        """Проверка редиректа по логотипу Яндекса"""
        with allure.step("Инициализация страниц"):
            main_page = MainPage(driver)

        with allure.step("1. Принимаем куки'"):
            main_page.click_on_cookia_button()

        with allure.step(
                "2. Нажать на логотип Яндекса и проверить, что в новом окне через редирект открылась главная страница Дзена"):
            main_page.click_yandex_logo_and_verify()