from selenium.webdriver.common.by import By

class TestLocators:
    URL ='https://stellarburgers.nomoreparties.site/' #сайт с бургерами
    # Тестовые данные для авторизации пользователя:
    TEST_LOGIN = "mikhailbesedin6666@yandex.ru"
    TEST_PAS = "besedin11221122"

    EMAIL_ENTRY_FIELD = By.XPATH, '//label[text()="Email"]/following-sibling::input'
    # ввод в строку Емейл
    PASSWORD_ENTRY_FIELD = By.XPATH, '//label[text()="Пароль"]/following-sibling::input'
    # ввод в строку Пароль
    NAME_ENTRY_FIELD = By.XPATH, '//label[text()="Имя"]/following-sibling::input'
    # ввод в строку Имя


    LOG_IN_TO_YOUR_PERSONAL_ACCOUNT = By.XPATH,'//*[text()="Личный Кабинет"]'
    #кнопка входа в ЛК
    BUTTON_REGISTER = By.XPATH,'//*[text()="Зарегистрироваться"]'
    #кнопка зарегистрироваться при вводе нового пользователя
    RESTORE_PASSWORD_BUTTON = By.XPATH, "//a[contains(text(),'Восстановить пароль')]"
    # кнопка Восстановить пароль

    BUTTON_GO_TO_ACCOUNT = By.XPATH, '//button[text()="Войти в аккаунт"]'
    # кнопка Войти в аккаунт
    LOGIN_BUTTON = By.XPATH,'//button[text()="Войти"]'
    #кнопка Войти при авторизации
    LOGIN_BUTTON_IN_THE_REGISTRATION_FORM = By.XPATH, '//a[contains(@class,"Auth_link")]'
    # кнопка Войти в форме регистрации
    LOGIN_BUTTON_IN_THE_RESTORE_PASSWORD_FORM = By.XPATH, "//a[contains(text(),'Войти')]"
    # кнопка Войти в форме восстановления пароля

    ERROR_PASSWORD = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p'
    # Ошибка на странице регистрации нового пользователя при вводе некорректного пароля
    TAG_ENTER = By.TAG_NAME, 'h2'
    # Заголовок на странице после резгистрации нового пользователя

    PROFILE_BUTTON = By.XPATH, '//a[contains(@class," Account_link_active")]'
    # кнопка Профиль
    EXIT_BUTTON = By.XPATH,'//button[contains(@class,"Account_button")]'
    # кнопка Выход


    STELLAR_BURGERS_LOGO = By.XPATH,'//*[contains(@class, "AppHeader_header__logo")]'
    #кнопка лого STELLAR_BURGERS в Личном кабинете.
    BUTTON_CONSTRUCTOR = By.XPATH, "//p[contains(text(),'Конструктор')]"
    # кнопка Конструктор в в Личном кабинете
    TITLE_IN_THE_CONSTRUCTOR = By.XPATH, '//h1[contains(@class, "text text_type_main-large")]'
    # Заголовок в конструкторе бургеров "Соберите бургер"

    BUTTON_BUNS = By.XPATH,'//span[text()="Булки"]'#кнопка Булки
    BUNS_SECTION_NAME = By.XPATH,'//h2[text()="Булки"]'#заголовок Булки
    BUTTON_SAUCES = By.XPATH,'//span[text()="Соусы"]'#кнопка Соусы
    SAUCES_SECTION_NAME = By.XPATH,'//h2[text()="Соусы"]'#заголовок Соусы
    BUTTON_FILLINGS = By.XPATH,'//span[text()="Начинки"]'#кнопка Начинки
    FILLINGS_SECTION_NAME = By.XPATH,'//h2[text()="Начинки"]'#заголовок Начинки

    PLACE_ORDER_BUTTON = By.XPATH, '//button[contains(@class,"button_button__33qZ0" )]'
    #кнопка Оформить заказ


