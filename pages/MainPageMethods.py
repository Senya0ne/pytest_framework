from .BaseMethods import BasePage
from locators.MainPageLocators import LocatorsMainPage
from selenium.webdriver.common.keys import Keys


class SearchHelper(BasePage):

    def enter_word(self, word):
        input = self.find_element(LocatorsMainPage.LOCATOR_INPUT)
        input.click()
        input.send_keys(word)
        input.send_keys(Keys.RETURN)
        return input

    def click_toggle(self):
        return self.find_element(LocatorsMainPage.LOCATOR_TOGGLE).click()