import pytest
from selenium.webdriver.support import expected_conditions as EC

from config import (
    EXPECTED_USER_NAME,
    MAIN_PAGE_URL,
)
from helpers import login, logout, register_new_user
from locators import (
    BTN_LOGIN_AND_REGISTER,
    BTN_USER_AVATAR,
    TXT_USER_NAME_IN_HEADER,
)


class TestLogin:
    """Авторизация пользователя (сценарий Test_4 из README)."""

    @pytest.mark.xfail(
        reason="Найден дефект: после входа приложение не переводит "
        "на главную страницу"
    )
    def test_successful_login_redirects_to_main_page(self, driver, wait):
        """Успешный вход: пользователь попадает на главную страницу."""
        email, password = register_new_user(driver, wait)
        logout(driver, wait)

        login(driver, wait, email, password)

        wait.until(EC.url_to_be(MAIN_PAGE_URL))

    def test_successful_login_shows_user_data_in_header(self, driver, wait):
        """Успешный вход: в правом верхнем углу рядом с кнопкой
        «Разместить объявление» отображаются аватар и имя User."""
        email, password = register_new_user(driver, wait)
        logout(driver, wait)

        login(driver, wait, email, password)

        wait.until(EC.visibility_of_element_located(BTN_USER_AVATAR))
        user_name = wait.until(
            EC.visibility_of_element_located(TXT_USER_NAME_IN_HEADER)
        )

        assert user_name.text == EXPECTED_USER_NAME, (
            f"Имя пользователя в хедере: ожидалось '{EXPECTED_USER_NAME}',"
            f" получено '{user_name.text}'"
        )


class TestLogout:
    """Выход из аккаунта (сценарий Test_5 из README)."""

    def test_logout_hides_user_data_and_shows_login_button(self, driver, wait):
        """После выхода аватар и имя User не отображаются, на их месте
        отображается кнопка «Вход и регистрация»."""
        register_new_user(driver, wait)

        logout(driver, wait)

        assert not driver.find_elements(*BTN_USER_AVATAR), (
            "Аватар пользователя всё ещё отображается в хедере"
        )
        assert not driver.find_elements(*TXT_USER_NAME_IN_HEADER), (
            "Имя пользователя всё ещё отображается в хедере"
        )
        assert driver.find_element(*BTN_LOGIN_AND_REGISTER).is_displayed(), (
            "Кнопка «Вход и регистрация» не отображается в правом верхнем углу"
        )
