import pytest

from tests.pages.site.main_page import MainPage
from tests.pages.site.constats import URL
import time


class TestMainPage:
    def test_exists_nav_text(self, browser):
        el = MainPage(browser, URL)
        el.open()
        expected_text = el.HEADERS_TITLE
        actual_text = el.get_headers_title()
        assert expected_text == actual_text, 'Validating Nav Likns text'

    def test_first_scroll_down(self, browser):
        el = MainPage(browser, URL)
        el.open()
        el.scroll_down_1_space()
        el.scroll_down_2_space()
        el.scroll_down_3_space()
        el.scroll_down_4_space()
        el.scroll_down_5_space()
        el.scroll_down_6_space()
        el.scroll_down_7_space()
        el.scroll_until_end()
        assert el.info_about_company() == "Юридическая информация", "Info about company"


