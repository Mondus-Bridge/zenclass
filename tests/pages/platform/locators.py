from selenium.webdriver.common.by import By

class LoginPageLocators:
    SIGNUP_LINK = (By.CSS_SELECTOR, ".nav-link:nth-child(1)")
    SIGNIN_LINK = (By.CSS_SELECTOR, ".nav-link:nth-child(2)")
    WITH_EMAIL = (By.CSS_SELECTOR, ".email-button")
    EMAIL_FIELD = (By.CSS_SELECTOR, ".z-input__field[type='email']")
    PHONE_FIELD = (By.CSS_SELECTOR, ".z-input__field[type='tel']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, ".z-input__field[type='password']")
    LOGGIN = (By.CSS_SELECTOR, ".btn.primary[type='submit']")
    IF_ERROR = (By.CLASS_NAME, ".error-message")
    WELCOME_CONTENT = (By.CSS_SELECTOR, ".layout.fill-height.wrap.fill-height")

    AVATAR = (By.CSS_SELECTOR, "div.flex div.z-avatar img[alt='Аватар']")
    AVATAR_INPUT = (By.CSS_SELECTOR, "input.z-file-uploader__input")
    AVATAR_SAVE_BUTTON = (By.CSS_SELECTOR, "div .flex.pr-16.py-8.xs6>button.z-btn > div.z-btn__content")
    NEWS_POPUP = (By.CSS_SELECTOR, ".popup__close-button-text")

    CONTINUE_SETTING =(By.XPATH, "//div[text()='Продолжить настройку']")
    FIRST_NAME = (By.CSS_SELECTOR, "div.owner-fields > div.z-input:nth-child(1)")
    LAST_NAME = (By.CSS_SELECTOR, "div.owner-fields > div.z-input:nth-child(2)")
    SEX_SELECTOR = (By.CSS_SELECTOR, "div.mb-24 > div.z-select")
    BIRTHDATE = (By.CSS_SELECTOR, "div.datetime-picker__date")

