from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):


    HEADERS_TITLE = 'Возможности,Интерфейс Zenclass,Журнал «Понятно»,Истории школ,Войти'

    def get_headers_title(self):
        nav_elements = WebDriverWait(self.browser, 10).until(EC.presence_of_all_elements_located(MainPageLocators.HEADERS_EL))
        nav_links_text = [link.text for link in nav_elements]
        return ",".join(nav_links_text)

    def scroll_down_1_space(self):
        element = self.browser.find_element(*MainPageLocators.ELEMENT_1)
        self.browser.execute_script('arguments[0].scrollIntoView(true);', element)

    def scroll_down_2_space(self):
        element = self.browser.find_element(*MainPageLocators.ELEMENT_2)
        self.browser.execute_script('arguments[0].scrollIntoView(true);', element)

    def scroll_down_3_space(self):
        element = self.browser.find_element(*MainPageLocators.ELEMENT_3)
        self.browser.execute_script('arguments[0].scrollIntoView(true);', element)

    def scroll_down_4_space(self):
        element = self.browser.find_element(*MainPageLocators.ELEMENT_4)
        self.browser.execute_script('arguments[0].scrollIntoView(true);', element)

    def scroll_down_5_space(self):
        element = self.browser.find_element(*MainPageLocators.ELEMENT_5)
        self.browser.execute_script('arguments[0].scrollIntoView(true);', element)

    def scroll_down_6_space(self):
        element = self.browser.find_element(*MainPageLocators.ELEMENT_6)
        self.browser.execute_script('arguments[0].scrollIntoView(true);', element)

    def scroll_down_7_space(self):
        element = self.browser.find_element(*MainPageLocators.ELEMENT_7)
        self.browser.execute_script('arguments[0].scrollIntoView(true);', element)

    def scroll_until_end(self):
        action = self.browser.find_element(By.TAG_NAME, "body")
        action.send_keys(Keys.END)

    def info_about_company(self):
        info = self.browser.find_element(*MainPageLocators.DOCS_ABOUT_COMPANY)
        return info.text







