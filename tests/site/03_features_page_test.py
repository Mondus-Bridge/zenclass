import pytest

from tests.pages.site.features_page import FeaturesPage
from tests.pages.site.constats import URL_FEATURES as URL, URL_SIGNUP
import time


class TestMainPage:
    def test_exists_nav_text(self, browser):
        el = FeaturesPage(browser, URL)
        el.open()
        el.scroll_until()
        assert el.should_be_sighup_link() == URL_SIGNUP, "Button start schooll doesn't have valid link"