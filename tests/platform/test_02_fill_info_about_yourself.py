from tests.pages.platform.fill_school_info import SchoolInfo
from tests.pages.platform.constants import MAIL, PASSWORD, BASE_lINK


def test_fill_first_form_after_sighin(browser):
    form = SchoolInfo(browser, BASE_lINK, MAIL, PASSWORD)
    form.open()
    form.user_and_pass()
    form.personal_info()
    form.upload_avatar()
    form.should_be_avatar_src()
