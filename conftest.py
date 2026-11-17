import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from config import MAIN_PAGE_URL


@pytest.fixture
def driver():
    """Создаёт инстанс браузера, открывает главную страницу,
    после теста закрывает браузер."""
    driver = webdriver.Chrome()
    driver.get(MAIN_PAGE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)
