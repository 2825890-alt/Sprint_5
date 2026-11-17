import uuid

from selenium.webdriver.support import expected_conditions as EC

from config import (
    EXPECTED_AUTH_MODAL_TITLE,
    PROFILE_PAGE_URL,
)
from helpers import find_created_listing, register_new_user
from locators import (
    BTN_CREATE_LISTING,
    BTN_PUBLISH_LISTING,
    CARD_LISTING_IN_PROFILE,
    DROPDOWN_CATEGORY_ARROW,
    DROPDOWN_CATEGORY_OPTION,
    DROPDOWN_CITY_ARROW,
    DROPDOWN_CITY_OPTION,
    INPUT_LISTING_DESCRIPTION,
    INPUT_LISTING_PRICE,
    INPUT_LISTING_TITLE,
    RADIO_CONDITION_NEW_LABEL,
    TITLE_AUTH_REQUIRED_MODAL,
    TITLE_CREATE_LISTING,
    TITLE_MY_LISTINGS,
)

LISTING_DESCRIPTION = "Хороший товар"
LISTING_PRICE = "600"


class TestCreateListing:
    """Создание объявления (сценарии Test_6, Test_7 из README)."""

    def test_unauthorized_user_cannot_create_listing(self, driver, wait):
        """Неавторизованный пользователь при нажатии «Разместить объявление»
        видит модальное окно с заголовком «Чтобы разместить объявление, авторизуйтесь»."""
        driver.find_element(*BTN_CREATE_LISTING).click()

        modal_title = wait.until(
            EC.visibility_of_element_located(TITLE_AUTH_REQUIRED_MODAL)
        )

        assert modal_title.text == EXPECTED_AUTH_MODAL_TITLE, (
            f"Заголовок модального окна: ожидался '{EXPECTED_AUTH_MODAL_TITLE}',"
            f" получен '{modal_title.text}'"
        )

    def test_authorized_user_can_create_listing(self, driver, wait):
        """Авторизованный пользователь публикует объявление, и оно
        отображается в блоке «Мои объявления» в профиле."""
        register_new_user(driver, wait)

        wait.until(EC.element_to_be_clickable(BTN_CREATE_LISTING)).click()
        wait.until(EC.visibility_of_element_located(TITLE_CREATE_LISTING))

        listing_title = f"Новый товар {uuid.uuid4()}"
        driver.find_element(*INPUT_LISTING_TITLE).send_keys(listing_title)
        driver.find_element(*INPUT_LISTING_DESCRIPTION).send_keys(LISTING_DESCRIPTION)
        driver.find_element(*INPUT_LISTING_PRICE).send_keys(LISTING_PRICE)

        driver.find_element(*DROPDOWN_CATEGORY_ARROW).click()
        wait.until(EC.element_to_be_clickable(DROPDOWN_CATEGORY_OPTION)).click()

        driver.find_element(*DROPDOWN_CITY_ARROW).click()
        wait.until(EC.element_to_be_clickable(DROPDOWN_CITY_OPTION)).click()

        driver.find_element(*RADIO_CONDITION_NEW_LABEL).click()

        driver.find_element(*BTN_PUBLISH_LISTING).click()
        wait.until(EC.invisibility_of_element_located(BTN_PUBLISH_LISTING))

        driver.get(PROFILE_PAGE_URL)
        wait.until(EC.visibility_of_element_located(TITLE_MY_LISTINGS))

        # Карточки в блоке «Мои объявления» подгружаются асинхронно —
        # дожидаемся появления первой, затем ищем созданное объявление
        wait.until(EC.visibility_of_any_elements_located(CARD_LISTING_IN_PROFILE))

        listing_card = find_created_listing(driver, wait, listing_title)
        assert listing_card is not None, (
            f"Объявление «{listing_title}» не найдено в блоке «Мои объявления»"
        )
