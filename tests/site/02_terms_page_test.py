from tests.pages.site.term_page import TermsPage
from tests.pages.site.constats import URL_TERM, URL


class TestMainPage:
    def test_exists_nav_text(self, browser):
        el = TermsPage(browser, URL_TERM)
        el.open()
        assert el.get_list_of_docs() == el.LIST_OF_DOCS, "Verifying list of docs in terms page"

    def test_back_to_main(self, browser):
        el = TermsPage(browser, URL_TERM)
        el.back_to_main()
        assert el.get_main_url() == URL, "Button get to main from terms page invalid"