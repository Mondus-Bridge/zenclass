from .locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self, browser, url, email, password):
        self.browser = browser
        self.url = url
        self.email = email
        self.password = password

    def open(self):
        self.browser.get(self.url)

    def user_and_pass(self):
        signin = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(LoginPageLocators.SIGNUP_LINK))
        signin.click()
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(LoginPageLocators.EMAIL_FIELD))
        email.send_keys(self.email)
        password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(LoginPageLocators.PASSWORD_FIELD))
        password.send_keys(self.password)
        loggin = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(LoginPageLocators.LOGGIN))
        loggin.click()