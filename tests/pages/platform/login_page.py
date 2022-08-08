from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .constants import LINK_SCHOOL_MAIN
import time


class LoginPage(BasePage):

    def register_new_user(self, email, phone ,password):
        signin = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(LoginPageLocators.SIGNIN_LINK))
        signin.click()
        withemail = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(LoginPageLocators.WITH_EMAIL))
        withemail.click()
        self.email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(LoginPageLocators.EMAIL_FIELD))
        self.email.send_keys(email)
        self.phone = self.browser.find_element(*LoginPageLocators.PHONE_FIELD)
        self.phone.send_keys(phone)
        self.password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(LoginPageLocators.PASSWORD_FIELD))
        self.password.send_keys(password)
        createUser = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(LoginPageLocators.LOGGIN))
        createUser.click()

    def should_be_welcome_form(self):
        assert WebDriverWait(self.browser, 30).until(EC.visibility_of_all_elements_located(LoginPageLocators.WELCOME_CONTENT)), "We don't have welcome form for new user"


    def signup(self, email, password):
        signup = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(LoginPageLocators.SIGNUP_LINK))
        signup.click()
        self.email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(LoginPageLocators.EMAIL_FIELD))
        self.email.send_keys(email)
        self.password = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(LoginPageLocators.PASSWORD_FIELD))
        self.password.send_keys(password)
        createUser = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(LoginPageLocators.LOGGIN))
        createUser.click()


    def should_be_your_school_url(self):
        time.sleep(5)
        get_url = self.browser.current_url
        assert  get_url[:31] in LINK_SCHOOL_MAIN, f"after login you see {get_url}, instead {LINK_SCHOOL_MAIN}"

