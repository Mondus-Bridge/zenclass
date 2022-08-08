from tests.pages.platform.login_page import LoginPage
from tests.pages.platform.constants import MAIL, PASSWORD, BASE_lINK


def test_login(browser):
    page = LoginPage(browser, BASE_lINK, MAIL, PASSWORD)
    page.open()
    page.user_and_pass()
    page.should_be_your_school_url()



    #page.register_new_user(NEW_MAIL, NEW_PHONE, NEW_PASSWORD)
    #page.should_be_welcome_form()
#