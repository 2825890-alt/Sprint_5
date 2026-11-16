from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from config import TEST_USER_EMAIL, TEST_USER_PASSWORD
import uuid

from locators import (
    BTN_CREATE_LISTING,
    TITLE_AUTH_REQUIRED_MODAL,
)

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("https://qa-desk.education-services.ru/")

#Нажать на кнопку Разместить объявление"
driver.find_element(*BTN_CREATE_LISTING).click()

modal_title = wait.until(expected_conditions.visibility_of_element_located(TITLE_AUTH_REQUIRED_MODAL))

expected_title = "Чтобы разместить объявление, авторизуйтесь"
assert modal_title.text == expected_title, (
    f"Неверный заголовок модального окна: "
    f"ожидали '{expected_title}', фактически '{modal_title.text}'"
)

driver.quit()