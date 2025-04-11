from base.locators import search_page_locators, parameters
from base.baseFunctions import BaseFunctions


class SearchFunctions(BaseFunctions):
    def __init__(self, driver):
        super().__init__(driver)

    def search(self):
        self.input(search_page_locators.search_textbox, parameters.search_text)
        self.click(search_page_locators.search)
        assert self.wait_for_element(search_page_locators.search_textbox).get_attribute("value") == parameters.search_text
        self.click(search_page_locators.second_page)

    def click_product(self):
        self.click(search_page_locators.product)