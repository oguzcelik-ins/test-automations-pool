from base.locators import product_page_locators
from base.baseFunctions import BaseFunctions


class ProductFunctions(BaseFunctions):
    def __init__(self, driver):
        super().__init__(driver)

    def add_to_wishlist(self):
        self.click(product_page_locators.add_to_wishlist)

    def navigate_to_wishlist_page(self):
        product_text = self.wait_for_element(product_page_locators.product_text).text
        self.click(product_page_locators.wishlist)
        assert product_text == self.wait_for_element(product_page_locators.in_wishlist_product_text).text

    def delete_product(self):
        product_text = self.wait_for_element(product_page_locators.in_wishlist_product_text).text
        self.click(product_page_locators.delete)
        assert product_text != self.wait_for_element(product_page_locators.in_wishlist_product_text).text