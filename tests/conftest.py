import pytest
from selenium import webdriver

from curl import main_site


@pytest.fixture(scope="function")
def driver():
    browser = webdriver.Firefox()
    browser.set_window_size(1600, 900)
    browser.get(main_site)
    yield browser
    browser.quit()
