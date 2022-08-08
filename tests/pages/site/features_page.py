from .base_page import BasePage
from .locators import FeaturesPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class FeaturesPage(BasePage):
    def scroll_until(self):
        element = WebDriverWait(self.browser,10).until(EC.presence_of_element_located(FeaturesPageLocators.PROTECT_CONTENT))
        self.browser.execute_script('arguments[0].scrollIntoView(true);', element)

    def should_be_sighup_link(self):
        slctr = self.browser.find_element(*FeaturesPageLocators.START_SCHOOL)
        val = slctr.get_attribute("href")
        return val


