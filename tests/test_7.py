from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import urlparse
from config import TEST_USER_EMAIL, TEST_USER_PASSWORD

import uuid

from locators import (
    BTN_LOGIN_AND_REGISTER,
    DROPDOWN_CITY_OPTION,
    DROPDOWN_CITY_ARROW,
    FORM_LOGIN_POPUP,
    INPUT_EMAIL_LOGIN,
    INPUT_PASSWORD_LOGIN,
    BTN_LOGIN_SUBMIT,
    INPUT_LISTING_PRICE,
    BTN_CREATE_LISTING,
    INPUT_LISTING_TITLE,
    INPUT_LISTING_DESCRIPTION,
    BTN_USER_AVATAR,
    BTN_PUBLISH_LISTING,
    TITLE_MY_LISTINGS,
    CARD_LISTING_IN_PROFILE,
    RADIO_CONDITION_NEW_LABEL,
    BTN_MY_LISTINGS_PAGINATION_NEXT
    
)

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("https://qa-desk.education-services.ru/")

# Нажать на кнопку "Вход и регистрация"
driver.find_element(*BTN_LOGIN_AND_REGISTER).click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(FORM_LOGIN_POPUP))

#Ввести email
valid_email = TEST_USER_EMAIL
driver.find_element(*INPUT_EMAIL_LOGIN).send_keys(valid_email)

#Ввести пароль
password = TEST_USER_PASSWORD
driver.find_element(*INPUT_PASSWORD_LOGIN).send_keys(password)

#Нажать на кнопку Войти
driver.find_element(*BTN_LOGIN_SUBMIT).click()

wait.until(expected_conditions.invisibility_of_element_located(FORM_LOGIN_POPUP))

#Нажать на кнопку Разместить объявление
driver.find_element(*BTN_CREATE_LISTING).click()

#Заполнить форму Название
listing_title = f"Новый товар {uuid.uuid4()}"
driver.find_element(*INPUT_LISTING_TITLE).send_keys(listing_title)

#Заполнить форму Описание товара
driver.find_element(*INPUT_LISTING_DESCRIPTION).send_keys("Хороший товар")

#Заполнить форму Стоимость
driver.find_element(*INPUT_LISTING_PRICE).send_keys("600")

#Открыть dropdown города
driver.find_element(*DROPDOWN_CITY_ARROW).click()

# Выбрать город «Москва»
wait.until(expected_conditions.element_to_be_clickable(DROPDOWN_CITY_OPTION)).click()

#Выбрать состояние Новый
driver.find_element(*RADIO_CONDITION_NEW_LABEL).click()

# Нажать кнопку «Опубликовать»
driver.find_element(*BTN_PUBLISH_LISTING).click()

# Дождаться завершения публикации
wait.until(expected_conditions.invisibility_of_element_located(BTN_PUBLISH_LISTING))

# Перейти на страницу профиля
driver.get("https://qa-desk.education-services.ru/profile")

wait.until(expected_conditions.visibility_of_element_located(TITLE_MY_LISTINGS))
wait.until(expected_conditions.visibility_of_any_elements_located(CARD_LISTING_IN_PROFILE))


def listing_is_present():
    """Ищет объявление по всем страницам «Мои объявления»."""
    page = 1
    while True:
        cards = driver.find_elements(*CARD_LISTING_IN_PROFILE)
        print(f"— Страница {page}, карточек: {len(cards)}")
        for c in cards:
            print("   •", c.text.splitlines()[0])
        if any(listing_title in c.text for c in cards):
            return True

        next_btns = driver.find_elements(*BTN_MY_LISTINGS_PAGINATION_NEXT)
        if not next_btns or not next_btns[0].is_displayed() or not next_btns[0].is_enabled():
            return False  # страниц больше нет — объявления нет
        next_btns[0].click()
        wait.until(expected_conditions.staleness_of(cards[0]))  # страница обновилась
        page += 1


found = listing_is_present()
assert found, f"Объявление «{listing_title}» не найдено в «Мои объявления»"
print(f"PASS: объявление «{listing_title}» отображается в «Мои объявления»")

driver.quit()





