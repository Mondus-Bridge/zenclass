from selenium.webdriver.common.by import By

class MainPageLocators:
    ZENCLASS_LOGO = (By.XPATH, "//img[@alt='Zenclass']")
    HEADERS = (By.CLASS_NAME, '.t228__centercontainer')
    HEADERS_EL = (By.CSS_SELECTOR, 'li.t228__list_item > a.t-menu__link-item')
    TEXT_IN_CENTER = (By.XPATH, "//h2[text()='С Zenclass просто!']")
    GRANNY_IN_CENTER = (By.CSS_SELECTOR, "img[src = 'https://static.tildacdn.com/tild6565-3736-4836-a564-376236653065/Group_83.svg']")
    ELEMENT_1 = (By.XPATH, "//h2[text()='С Zenclass просто!']")
    ELEMENT_2 = (By.XPATH, "//h2[text()='Просто начать']")
    ELEMENT_3 = (By.XPATH, "//h2[text()='Просто обучать']")
    ELEMENT_4 = (By.XPATH, "//h2[text()='Просто продавать']")
    ELEMENT_5 = (By.XPATH, "//h3[text()='Встроенный приём платежей Zenclass с бесплатной онлайн-кассой']")
    ELEMENT_6 = (By.XPATH, "//h3[text()='Интеграции с платёжными системами']")
    ELEMENT_7 = (By.XPATH, "//div[text() ='7 290 руб.']")
    DOCS_ABOUT_COMPANY = (By.XPATH, "//a[@href='/terms']")

class TermsPageLocators:
    LIST_OF_DOCS = (By.CSS_SELECTOR, "div.t-text.t-text_md > a")
    BACK_TO_MAIN = (By.XPATH, "//a[text() = 'Вернуться на главную']")

class FeaturesPageLocators:
    ZENCLASS_LOGO = (By.XPATH, "//img[@alt='Zenclass']")
    PROTECT_CONTENT = (By.XPATH, "//strong[text()='Защита контента']")
    START_SCHOOL = (By.XPATH, "//a[text()='Запустить школу']")
