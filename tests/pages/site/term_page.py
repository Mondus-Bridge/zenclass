from .base_page import BasePage
from .locators import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class TermsPage(BasePage):

    LIST_OF_DOCS = 'Реквизиты юридического лица,Политика конфиденциальности,Лицензионное соглашение,Агентский договор-оферта (АД),Реферальная программа,Тарифы на использование платформы,Тарифы на использование услуги "Интернет-эквайринг ZenClass и онлайн касса"'
    def get_list_of_docs(self):
        el = WebDriverWait(self.browser, 10).until(EC.presence_of_all_elements_located(TermsPageLocators.LIST_OF_DOCS))
        el_text = [link.text for link in el]
        return ",".join(el_text)

    def back_to_main(self):
        action = self.browser.find_element(By.TAG_NAME, "body")
        action.send_keys(Keys.END)
        el = self.browser.find_element(*TermsPageLocators.BACK_TO_MAIN)
        el.click()
        time.sleep(1)

    def get_main_url(self):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(MainPageLocators.ZENCLASS_LOGO))
        get_url = self.browser.current_url
        return get_url