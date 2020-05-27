from pages.MainPageMethods import SearchHelper
import pytest

@pytest.mark.smoke
def test_main_page_input(browser):
    driver = SearchHelper(browser)
    driver.go_to_site()
    driver.enter_word('ololo')
    driver.enter_word('pain')
    driver.click_toggle()
