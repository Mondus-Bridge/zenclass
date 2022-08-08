from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .constants import AVATAR_PATH, FIRST_NAME, LAST_NAME,BIRTHDATE
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

from .locators import LoginPageLocators


class SchoolInfo(BasePage):

    def close_popup(self):
        popupButton = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(LoginPageLocators.NEWS_POPUP))
        popupButton.click()

    def upload_avatar(self):
        avatar = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(LoginPageLocators.AVATAR))
        avatar.click()
        avatarInput = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(LoginPageLocators.AVATAR_INPUT))
        avatarInput.send_keys(AVATAR_PATH)
        time.sleep(3) #обязтельно нужно время, чтобы загрузить файл
        saveAvatar = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(LoginPageLocators.AVATAR_SAVE_BUTTON))
        saveAvatar.click()

    def should_be_avatar_src(self):
        avatar = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(LoginPageLocators.AVATAR))
        atr = avatar.get_attribute("src")
        assert "https://zenclass-stage-files-hot.storage.yandexcloud.net/" in atr, "your image is not uploaded to server"

    try:
        def personal_info(self):
            continue_setting_button = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(LoginPageLocators.CONTINUE_SETTING))
            continue_setting_button.click()
            first_name = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(LoginPageLocators.FIRST_NAME))
            ActionChains(self.browser).move_to_element(first_name).click().perform()
            first_name.send_keys(FIRST_NAME)
            last_name = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(LoginPageLocators.LAST_NAME))
            ActionChains(self.browser).move_to_element(last_name).click().perform()
            last_name.send_keys(LAST_NAME)
            # last_name.send_keys(LAST_NAME)
            # sex_select = Select(self.browser(LoginPageLocators.SEX_SELECTOR))
            # sex_select.select_by_index(1)
            # birthdate = self.browser.find_element(LoginPageLocators.BIRTHDATE)
            # birthdate.send_keys(BIRTHDATE)
    except Exception:
        print(error)

