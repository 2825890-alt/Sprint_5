"""Повторяющиеся шаги сценариев, вынесенные из тестовых файлов."""
import uuid

from selenium.webdriver.support import expected_conditions as EC

from config import DEFAULT_USER_PASSWORD
from locators import (
    BTN_CREATE_ACCOUNT,
    BTN_LOGIN_AND_REGISTER,
    BTN_LOGIN_SUBMIT,
    BTN_LOGOUT,
    BTN_MY_LISTINGS_PAGINATION_NEXT,
    BTN_NO_ACCOUNT,
    BTN_USER_AVATAR,
    CARD_LISTING_IN_PROFILE,
    FORM_LOGIN_POPUP,
    INPUT_EMAIL_LOGIN,
    INPUT_EMAIL_REGISTRATION,
    INPUT_PASSWORD_LOGIN,
    INPUT_PASSWORD_REGISTRATION,
    INPUT_PASSWORD_REPEAT,
    TITLE_REGISTRATION,
)


def get_unique_email():
    """Генерирует уникальный email для регистрации нового пользователя."""
    return f"user_{uuid.uuid4().hex[:8]}@gmail.com"


def get_unique_listing_title():
    """Генерирует уникальное название для нового объявления."""
    return f"Новый товар {uuid.uuid4()}"


def open_registration_form(driver, wait):
    """Открывает попап «Вход и регистрация» и переходит к форме «Зарегистрироваться»."""
    driver.find_element(*BTN_LOGIN_AND_REGISTER).click()
    wait.until(EC.visibility_of_element_located(FORM_LOGIN_POPUP))
    driver.find_element(*BTN_NO_ACCOUNT).click()
    wait.until(EC.visibility_of_element_located(TITLE_REGISTRATION))


def fill_registration_form_and_submit(driver, email, password):
    """Заполняет все поля формы регистрации и нажимает «Создать аккаунт»."""
    driver.find_element(*INPUT_EMAIL_REGISTRATION).send_keys(email)
    driver.find_element(*INPUT_PASSWORD_REGISTRATION).send_keys(password)
    driver.find_element(*INPUT_PASSWORD_REPEAT).send_keys(password)
    driver.find_element(*BTN_CREATE_ACCOUNT).click()


def register_new_user(driver, wait):
    """Регистрирует нового пользователя и возвращает (email, пароль).
    После регистрации пользователь уже авторизован в приложении."""
    email = get_unique_email()
    password = DEFAULT_USER_PASSWORD
    open_registration_form(driver, wait)
    fill_registration_form_and_submit(driver, email, password)
    wait.until(EC.element_to_be_clickable(BTN_USER_AVATAR))
    return email, password


def login(driver, wait, email, password):
    """Входит под пользователем с указанными email и паролем."""
    driver.find_element(*BTN_LOGIN_AND_REGISTER).click()
    wait.until(EC.visibility_of_element_located(INPUT_EMAIL_LOGIN))
    driver.find_element(*INPUT_EMAIL_LOGIN).send_keys(email)
    driver.find_element(*INPUT_PASSWORD_LOGIN).send_keys(password)
    driver.find_element(*BTN_LOGIN_SUBMIT).click()


def logout(driver, wait):
    """Выходит из аккаунта авторизованного пользователя."""
    wait.until(EC.element_to_be_clickable(BTN_USER_AVATAR)).click()
    driver.find_element(*BTN_LOGOUT).click()
    wait.until(EC.element_to_be_clickable(BTN_LOGIN_AND_REGISTER))


def find_created_listing(driver, wait, listing_title):
    """Ищет объявление по заголовку на всех страницах блока
    «Мои объявления». Возвращает карточку-элемент или None."""
    while True:
        cards = driver.find_elements(*CARD_LISTING_IN_PROFILE)
        for card in cards:
            if listing_title in card.text:
                return card

        next_buttons = driver.find_elements(*BTN_MY_LISTINGS_PAGINATION_NEXT)
        if (
            not next_buttons
            or not next_buttons[0].is_displayed()
            or not next_buttons[0].is_enabled()
        ):
            return None
        next_buttons[0].click()
        wait.until(EC.staleness_of(cards[0]))
