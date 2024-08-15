from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    NAME_INPUT = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')
    EMAIL_INPUT = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    PASSWORD_INPUT = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')
    SUBMIT_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]')
    ERROR_MESSAGE = (By.XPATH, '//p[contains(text(), "Некорректный пароль")]')

class SignInMain:
    element_value = (By.XPATH, '//input[@value="gold_kas@mail.ru"]')
    ORDER_BUTTON = (By.XPATH,  '//button[contains(@class, "button_button__33qZ0") '
                               'and contains(@class, "button_button_type_primary__1O7Bx") '
                               'and contains(@class, "button_button_size_large__G21Vg")]')
    element_modal = (By.CSS_SELECTOR, 'div.Modal_modal_overlay__x2ZCr')
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    SUBMIT_TEXT_LK = (By.LINK_TEXT, "Личный Кабинет")
    SUBMIT_LOGIN = (By.CSS_SELECTOR, 'a[href="/login"]')
    SUBMIT_CONSTRUCTOR = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    SUBMIT_EXIT = (By.XPATH, "//button[text()='Выход']")
    SUBMIT_SIGNIN = (By.XPATH, '//button[text()="Войти"]')
    NAME_INPUT = (By.NAME, 'name')
    PASSWORD_INPUT = (By.NAME, 'Пароль')
    SUBMIT_BUTTON_SIGN_IN = (By.XPATH, "//button[contains(text(),'Войти')]")
    PROFILE_LINK = (By.XPATH, '//a[@href="/account/profile" and contains(@class, "Account_link_active__2opc9")]')
    SUBMIT_LK = (By.XPATH, '//p[contains(text(),"Личный Кабинет")]')
    CURR_NAME123 = (By.XPATH, '//input[@name="name"]')
    CURR_NAME = (By.XPATH, '//input[@name="name" and @value="gold_kas@mail.ru]')
    CURR_NAME_DIS = (By.XPATH, '//input[@name="name" and @value="gold_kas@mail.ru" and @disabled]')
    SAUCES_TEXT = (By.XPATH, '//div[span[text()="Соусы"]]')
    FILLINGS_TEXT = (By.XPATH, '//div[span[text()="Начинки"]]')
    BUNS_TEXT = (By.XPATH, '//div[span[text()="Булки"]]')
    constrfindtab = (By.XPATH, "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 "
                               "noselect']/span[@class='text text_type_main-default']")