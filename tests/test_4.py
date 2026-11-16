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
    BTN_CREATE_LISTING,
    TXT_USER_NAME_IN_HEADER,
)


EXPECTED_HOST = "qa-desk.education-services.ru"
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

# Проверка 1: произошёл переход на главную страницу
wait.until(expected_conditions.url_to_be("https://" + EXPECTED_HOST + "/"))

parsed_url = urlparse(driver.current_url)
assert parsed_url.netloc == EXPECTED_HOST and parsed_url.path in ("", "/"), \
    f"Ожидался переход на главную страницу, получен URL: '{driver.current_url}'"



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

