from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import urlparse

import uuid

from locators import (
    BTN_LOGIN_AND_REGISTER,
    BTN_NO_ACCOUNT,
    TITLE_REGISTRATION,
    FORM_LOGIN_POPUP,
    INPUT_EMAIL_REGISTRATION,
    INPUT_PASSWORD_REGISTRATION,
    INPUT_PASSWORD_REPEAT,
    BTN_CREATE_ACCOUNT,
    BTN_CREATE_LISTING,
    BTN_USER_AVATAR,
    TXT_USER_NAME_IN_HEADER,
)
EXPECTED_HOST = "qa-desk.education-services.ru"
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("https://qa-desk.education-services.ru/")

# Нажать на кнопку "Вход и регистрация"
driver.find_element(*BTN_LOGIN_AND_REGISTER).click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(FORM_LOGIN_POPUP))

# Нажать на кнопку "Нет аккаунта"
driver.find_element(*BTN_NO_ACCOUNT).click()


#Дождаться появления окна "Зарегистрироваться"
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TITLE_REGISTRATION))

#Ввести email
email = f"user_{uuid.uuid4().hex[:8]}@gmail.com"
driver.find_element(*INPUT_EMAIL_REGISTRATION).send_keys(email)

#Ввести пароль
password = "1234"
driver.find_element(*INPUT_PASSWORD_REGISTRATION).send_keys(password)

#Ввести пароль повторно
driver.find_element(*INPUT_PASSWORD_REPEAT).send_keys(password)

#Нажать кнопку "Создать аккаунт"
driver.find_element(*BTN_CREATE_ACCOUNT).click()



# Проверка 1: произошёл переход на главную страницу

wait.until(expected_conditions.url_to_be("https://" + EXPECTED_HOST + "/"))

parsed_url = urlparse(driver.current_url)
assert parsed_url.netloc == EXPECTED_HOST and parsed_url.path in ("", "/"), \
    f"Ожидался переход на главную страницу, получен URL: '{driver.current_url}'"


wait.until(expected_conditions.invisibility_of_element_located(BTN_LOGIN_AND_REGISTER))

# Проверка 2: аватар и имя "User" в правом верхнем углу,
# рядом с кнопкой «Разместить объявление»
wait.until(expected_conditions.element_to_be_clickable(BTN_CREATE_LISTING))

avatar = wait.until(expected_conditions.visibility_of_element_located(BTN_USER_AVATAR))
user_name = wait.until(expected_conditions.visibility_of_element_located(TXT_USER_NAME_IN_HEADER))

assert user_name.text == "User.", \
    f"Имя пользователя должно быть 'User.', получено: '{user_name.text}'"

assert abs(avatar.rect["y"] - driver.find_element(*BTN_CREATE_LISTING).rect["y"]) < 50, \
        "Аватар должен быть в одной строке с кнопкой «Разместить объявление»"

driver.quit()