# Константы проекта: URL, тестовые данные, ожидаемые значения интерфейса

BASE_URL = "https://qa-desk.education-services.ru"
MAIN_PAGE_URL = f"{BASE_URL}/"
PROFILE_PAGE_URL = f"{BASE_URL}/profile"

# Данные для регистрации новых пользователей в тестах
DEFAULT_USER_PASSWORD = "1234"

# Зарезервировано: заранее созданный тестовый пользователь.
# ВНИМАНИЕ: на текущем стенде вход с этими данными не проходит
# («Логин или пароль неверны»), поэтому тесты создают собственного
# пользователя через регистрацию.
TEST_USER_EMAIL = "qa_user_2@gmail.com"
TEST_USER_PASSWORD = "1234"

# Ожидаемые значения интерфейса
EXPECTED_USER_NAME = "User."
EXPECTED_ERROR_MESSAGE = "Ошибка"
EXPECTED_AUTH_MODAL_TITLE = "Чтобы разместить объявление, авторизуйтесь"
