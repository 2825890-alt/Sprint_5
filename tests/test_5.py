from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from config import TEST_USER_EMAIL, TEST_USER_PASSWORD
import uuid

from locators import (
    BTN_LOGIN_AND_REGISTER,
    BTN_USER_AVATAR,
    INPUT_EMAIL_LOGIN,
    INPUT_PASSWORD_LOGIN,
    BTN_LOGIN_SUBMIT,
    BTN_LOGOUT,
    BTN_CREATE_LISTING,
    TXT_USER_NAME_IN_HEADER,
)

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("https://qa-desk.education-services.ru/")

#Нажать на кнопку "Вход и регистрация"
driver.find_element(*BTN_LOGIN_AND_REGISTER).click()


wait.until(expected_conditions.visibility_of_element_located(INPUT_EMAIL_LOGIN))

#Ввести email
valid_email = TEST_USER_EMAIL
driver.find_element(*INPUT_EMAIL_LOGIN).send_keys(valid_email)

#Ввести пароль
password = TEST_USER_PASSWORD
driver.find_element(*INPUT_PASSWORD_LOGIN).send_keys(password)

#Нажать на кнопку Войти
driver.find_element(*BTN_LOGIN_SUBMIT).click()

wait.until(expected_conditions.visibility_of_element_located(TXT_USER_NAME_IN_HEADER))
wait.until(expected_conditions.element_to_be_clickable(BTN_USER_AVATAR))
#Выйти из аккаунта
driver.find_element(*BTN_USER_AVATAR).click()

driver.find_element(*BTN_LOGOUT).click()

wait.until(expected_conditions.element_to_be_clickable(BTN_LOGIN_AND_REGISTER))


assert not driver.find_elements(*BTN_USER_AVATAR), \
    "Аватар пользователя всё ещё отображается около кнопки 'Разместить объявление'"
assert not driver.find_elements(*TXT_USER_NAME_IN_HEADER), \
    "Имя пользователя всё ещё отображается около кнопки 'Разместить объявление'"

login_btn = driver.find_element(*BTN_LOGIN_AND_REGISTER)
assert login_btn.is_displayed(), \
    "Кнопка 'Вход и регистрация' не отображается в правом верхнем углу"



driver.quit()