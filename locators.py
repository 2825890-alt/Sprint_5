from selenium.webdriver.common.by import By

# Кнопка «Вход и регистрация» (до авторизации)
BTN_LOGIN_AND_REGISTER = (By.XPATH, "//button[normalize-space()='Вход и регистрация']")

# Кнопка «Разместить объявление»
BTN_CREATE_LISTING = (By.XPATH, "//button[normalize-space()='Разместить объявление']")

# Аватар пользователя в хедере (кнопка вокруг аватара, ведёт в профиль)
BTN_USER_AVATAR = (By.CSS_SELECTOR, "button.circleSmall")

# Картинка аватара (если загружено фото; иначе SVG-заглушка class="svgSmall")
IMG_USER_AVATAR = (By.CSS_SELECTOR, "img.avatarSmall")

# Имя пользователя в хедере
TXT_USER_NAME_IN_HEADER = (By.XPATH,
    "//h3[contains(@class,'profileText') and contains(@class,'name')]")

# Поле «Имя» на форме регистрации
INPUT_NAME_REGISTRATION = (By.XPATH, "//input[@name='name' and @placeholder='Имя']")

# Кнопка «Выйти»
BTN_LOGOUT = (By.XPATH, "//button[normalize-space()='Выйти']")

# Контейнер попапа авторизации
FORM_LOGIN_POPUP = (By.XPATH, "//form[starts-with(@class,'popUp_shell')]")

# Поле Email
INPUT_EMAIL_LOGIN = (By.XPATH, "//input[@name='email' and @placeholder='Введите Email']")

# Поле Пароль (type='password' уникализирует среди полей)
INPUT_PASSWORD_LOGIN = (By.XPATH, "//input[@name='password' and @type='password']")

# Кнопка «Войти» 
BTN_LOGIN_SUBMIT = (By.XPATH, "//button[@type='submit' and normalize-space()='Войти']")

# Кнопка «Нет аккаунта» (переход к регистрации)
BTN_NO_ACCOUNT = (By.XPATH, "//button[normalize-space()='Нет аккаунта']")

# Кнопка-крестик закрытия попапа 
BTN_CLOSE_POPUP = (By.XPATH, "//button[contains(@class,'popUp_XBtn__')]")

# Контейнер формы регистрации
FORM_REGISTRATION_POPUP = (By.XPATH, "//form[starts-with(@class,'popUp_shell')]")

# Заголовок формы «Зарегистрироваться»
TITLE_REGISTRATION = (By.XPATH, "//h1[normalize-space()='Зарегистрироваться']")

# Поле Email
INPUT_EMAIL_REGISTRATION = (By.XPATH, "//input[@name='email' and @placeholder='Введите Email']")

# Поле Пароль
INPUT_PASSWORD_REGISTRATION = (By.XPATH, "//input[@name='password' and @placeholder='Пароль']")

# Поле «Повторите пароль»
INPUT_PASSWORD_REPEAT = (By.XPATH, "//input[@name='submitPassword']")

# Кнопка «Создать аккаунт» 
BTN_CREATE_ACCOUNT = (By.XPATH,
    "//button[@type='submit' and normalize-space()='Создать аккаунт']")

# Обёртка поля Email в состоянии ошибки (красная подсветка)
DIV_EMAIL_FIELD_ERROR = (By.XPATH,
    "//div[starts-with(@class,'input_inputError__')][.//input[@name='email']]")

# Обёртка поля Пароль в состоянии ошибки
DIV_PASSWORD_FIELD_ERROR = (By.XPATH,
    "//div[starts-with(@class,'input_inputError__')][.//input[@name='password']]")

# Обёртка поля «Повторите пароль» в состоянии ошибки
DIV_PASSWORD_REPEAT_FIELD_ERROR = (By.XPATH,
    "//div[starts-with(@class,'input_inputError__')][.//input[@name='submitPassword']]")

# Сообщение об ошибке под полем Email (текст «Ошибка»)
TXT_EMAIL_ERROR_MESSAGE = (By.XPATH,
    "//span[starts-with(@class,'input_span__')][normalize-space()='Ошибка']")

# Заголовок модального окна "Чтобы разместить объявление авторизуйтесь"
TITLE_AUTH_REQUIRED_MODAL = (By.XPATH,
    "//h1[normalize-space()='Чтобы разместить объявление, авторизуйтесь']") 

# Заголовок страницы «Новое объявление»
TITLE_CREATE_LISTING = (By.XPATH, "//h1[normalize-space()='Новое объявление']")

# Поле «Название»
INPUT_LISTING_TITLE = (By.XPATH, "//input[@name='name' and @placeholder='Название']")

# Поле «Описание товара» (textarea)
INPUT_LISTING_DESCRIPTION = (By.XPATH, "//textarea[@name='description']")

# Поле «Стоимость»
# ВАЖНО: type="text", а не number — числовой формат проверяется логикой приложения
INPUT_LISTING_PRICE = (By.XPATH, "//input[@name='price' and @placeholder='Стоимость']")

# Dropdown «Категория» — readonly-поле со значением
DROPDOWN_CATEGORY_VALUE = (By.XPATH, "//input[@name='category']")

# Кнопка-стрелка (открыть список категорий) — находится внутри контейнера поля «Категория»
DROPDOWN_CATEGORY_ARROW = (By.XPATH,
    "//div[contains(@class,'dropDownMenu_input__')][.//input[@name='category']]/button")

# Опция списка категорий — подставить нужное значение: 'Авто','Книги','Садоводство','Хобби','Технологии'
DROPDOWN_CATEGORY_OPTION = (By.XPATH,
    "//button[starts-with(@class,'dropDownMenu_btn__')]"
    "[.//span[normalize-space()='Авто']]")

# Dropdown «Город» — readonly-поле со значением
DROPDOWN_CITY_VALUE = (By.XPATH, "//input[@name='city']")

# Кнопка-стрелка (открыть список городов)
DROPDOWN_CITY_ARROW = (By.XPATH,
    "//div[contains(@class,'dropDownMenu_input__')][.//input[@name='city']]/button")

# Опция списка городов 
DROPDOWN_CITY_OPTION = (By.XPATH,
    "//button[starts-with(@class,'dropDownMenu_btn__')]"
    "[.//span[normalize-space()='Москва']]")

# RadioButton «Новый» — кликабельный label
RADIO_CONDITION_NEW_LABEL = (By.XPATH, "//label[normalize-space()='Новый']")

# RadioButton «Б/У» — кликабельный label
RADIO_CONDITION_USED_LABEL = (By.XPATH, "//label[normalize-space()='Б/У']")

# Скрытые input radio для проверки checked-состояния
RADIO_CONDITION_NEW_INPUT = (By.XPATH,
    "//input[@type='radio' and @name='condition' and @value='Новый']")
RADIO_CONDITION_USED_INPUT = (By.XPATH,
    "//input[@type='radio' and @name='condition' and @value='Б/У']")

# Кнопка «Опубликовать» (submit)
BTN_PUBLISH_LISTING = (By.XPATH,
    "//button[@type='submit' and normalize-space()='Опубликовать']")

# Заголовок блока «Мои объявления»
TITLE_MY_LISTINGS = (By.XPATH, "//h1[normalize-space()='Мои объявления']")

# Пустое состояние блока
TXT_MY_LISTINGS_EMPTY = (By.XPATH, "//h2[normalize-space()='Здесь пока пусто...']")

# Блок «Мои объявления» 
BLOCK_MY_LISTINGS = (By.XPATH,
    "//div[starts-with(@class,'profilePage_listningBlock__')]"
    "[.//h1[normalize-space()='Мои объявления']]")

# Карточка объявления внутри именно блока «Мои объявления»
CARD_LISTING_IN_PROFILE = (By.XPATH,
    "//div[starts-with(@class,'profilePage_listningBlock__')]"
    "[.//h1[normalize-space()='Мои объявления']]"
    "//div[contains(@class,'card')]")

# Кнопка «следующая страница» пагинации в блоке «Мои объявления»
BTN_MY_LISTINGS_PAGINATION_NEXT = (By.XPATH,
    "//div[starts-with(@class,'profilePage_listningBlock__')]"
    "[.//h1[normalize-space()='Мои объявления']]"
    "//button[contains(@class,'arrowButton--right')]")
