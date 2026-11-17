import pytest
from selenium.webdriver.support import expected_conditions as EC

from config import (
    DEFAULT_USER_PASSWORD,
    EXPECTED_ERROR_MESSAGE,
    EXPECTED_USER_NAME,
    MAIN_PAGE_URL,
)
from helpers import (
    fill_registration_form_and_submit,
    get_unique_email,
    logout,
    open_registration_form,
    register_new_user,
)
from locators import (
    BTN_USER_AVATAR,
    DIV_EMAIL_FIELD_ERROR,
    DIV_PASSWORD_FIELD_ERROR,
    DIV_PASSWORD_REPEAT_FIELD_ERROR,
    TXT_EMAIL_ERROR_MESSAGE,
    TXT_USER_NAME_IN_HEADER,
)


class TestRegistration:
    """Регистрация пользователя (сценарии Test_1, Test_2, Test_3 из README)."""

    @pytest.mark.xfail(
        reason="Найден дефект: после регистрации приложение не переводит "
        "на главную страницу — фактический URL /regiatration"
    )
    def test_new_user_registration_redirects_to_main_page(self, driver, wait):
        """Успешная регистрация: пользователь попадает на главную страницу."""
        open_registration_form(driver, wait)
        fill_registration_form_and_submit(
            driver, get_unique_email(), DEFAULT_USER_PASSWORD
        )

        wait.until(EC.url_to_be(MAIN_PAGE_URL))

    def test_new_user_registration_shows_user_data_in_header(self, driver, wait):
        """Успешная регистрация: в правом верхнем углу рядом с кнопкой
        «Разместить объявление» отображаются аватар и имя User."""
        open_registration_form(driver, wait)
        fill_registration_form_and_submit(
            driver, get_unique_email(), DEFAULT_USER_PASSWORD
        )

        wait.until(EC.visibility_of_element_located(BTN_USER_AVATAR))
        user_name = wait.until(
            EC.visibility_of_element_located(TXT_USER_NAME_IN_HEADER)
        )

        assert user_name.text == EXPECTED_USER_NAME, (
            f"Имя пользователя в хедере: ожидалось '{EXPECTED_USER_NAME}',"
            f" получено '{user_name.text}'"
        )

    def test_registration_with_invalid_email_shows_validation_errors(
        self, driver, wait
    ):
        """Регистрация с email не по маске: поля формы подсвечены красным,
        под полем Email отображается сообщение «Ошибка»."""
        open_registration_form(driver, wait)
        invalid_email = get_unique_email().replace("@", "")
        fill_registration_form_and_submit(driver, invalid_email, DEFAULT_USER_PASSWORD)

        wait.until(EC.visibility_of_element_located(DIV_EMAIL_FIELD_ERROR))
        wait.until(EC.visibility_of_element_located(DIV_PASSWORD_FIELD_ERROR))
        wait.until(
            EC.visibility_of_element_located(DIV_PASSWORD_REPEAT_FIELD_ERROR)
        )

        error_message = wait.until(
            EC.visibility_of_element_located(TXT_EMAIL_ERROR_MESSAGE)
        )
        assert error_message.text == EXPECTED_ERROR_MESSAGE, (
            f"Сообщение под полем Email: ожидалось '{EXPECTED_ERROR_MESSAGE}',"
            f" получено '{error_message.text}'"
        )

    def test_registration_with_existing_user_shows_validation_errors(
        self, driver, wait
    ):
        """Регистрация с email уже существующего пользователя: поля формы
        подсвечены красным, под полем Email отображается сообщение «Ошибка»."""
        existing_user_email, existing_user_password = register_new_user(driver, wait)
        logout(driver, wait)

        open_registration_form(driver, wait)
        fill_registration_form_and_submit(
            driver, existing_user_email, existing_user_password
        )

        wait.until(EC.visibility_of_element_located(DIV_EMAIL_FIELD_ERROR))
        wait.until(EC.visibility_of_element_located(DIV_PASSWORD_FIELD_ERROR))
        wait.until(
            EC.visibility_of_element_located(DIV_PASSWORD_REPEAT_FIELD_ERROR)
        )

        error_message = wait.until(
            EC.visibility_of_element_located(TXT_EMAIL_ERROR_MESSAGE)
        )
        assert error_message.text == EXPECTED_ERROR_MESSAGE, (
            f"Сообщение под полем Email: ожидалось '{EXPECTED_ERROR_MESSAGE}',"
            f" получено '{error_message.text}'"
        )
