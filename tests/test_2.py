from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import uuid

from locators import (
    BTN_LOGIN_AND_REGISTER,
    BTN_NO_ACCOUNT,
    TITLE_REGISTRATION,
    INPUT_EMAIL_REGISTRATION,
    INPUT_PASSWORD_REGISTRATION,
    INPUT_PASSWORD_REPEAT,
    BTN_CREATE_ACCOUNT,
    TXT_EMAIL_ERROR_MESSAGE,
    DIV_EMAIL_FIELD_ERROR,
    DIV_PASSWORD_FIELD_ERROR,
    DIV_PASSWORD_REPEAT_FIELD_ERROR,
)

ERROR_EMAIL_MSG = "Ошибка"

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("https://qa-desk.education-services.ru/")

#Нажать на кнопку "Вход и регистрация"
driver.find_element(*BTN_LOGIN_AND_REGISTER).click()

#Нажать на кнопку "Нет аккаунта"
driver.find_element(*BTN_NO_ACCOUNT).click()

#Дождаться появления окна "Зарегистрироваться"
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TITLE_REGISTRATION))

#Ввести email не по максе (отсутствует @)
invalid_email = f"user_{uuid.uuid4().hex[:8]}gmail.com"
driver.find_element(*INPUT_EMAIL_REGISTRATION).send_keys(invalid_email)

#Ввести пароль
password = "1234"
driver.find_element(*INPUT_PASSWORD_REGISTRATION).send_keys(password)

#Ввести пароль повторно
driver.find_element(*INPUT_PASSWORD_REPEAT).send_keys(password)

#Нажать кнопку "Создать аккаунт"
driver.find_element(*BTN_CREATE_ACCOUNT).click()

# Проверка 1. Поля выделены красным:

errors = []
for error_locator, name in [
        (DIV_EMAIL_FIELD_ERROR, "Email"),
        (DIV_PASSWORD_FIELD_ERROR, "Пароль"),
        (DIV_PASSWORD_REPEAT_FIELD_ERROR, "Повторите пароль"),
    ]:
    try:
        wait.until(expected_conditions.visibility_of_element_located(error_locator))
    except TimeoutException:
        errors.append(f"Поле '{name}' не подсвечено красным")
    

# Проверка 2. Под полем Email отображается сообщение "Ошибка"
try:
    error_msg = wait.until(
        expected_conditions.visibility_of_element_located(TXT_EMAIL_ERROR_MESSAGE))
except TimeoutException:
    error_msg = None
    errors.append("Сообщение об ошибке под полем Email не отображается")

if error_msg and error_msg.text.strip() != ERROR_EMAIL_MSG:
    errors.append(f"Сообщение: получено '{error_msg.text}', ожидалось '{ERROR_EMAIL_MSG}'")

assert not errors, "\n".join(errors)


driver.quit()        