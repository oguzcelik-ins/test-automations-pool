import time

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
        assert product_text == self.wait_for_element(product_page_locators.in_wishlist_product_text).text, \
            "Text's are not matched!"

    def delete_product(self):
        product_text = self.wait_for_element(product_page_locators.in_wishlist_product_text).text
        self.click(product_page_locators.delete)
        time.sleep(2)
        assert self.wait_for_element(product_page_locators.deleted_text), "Product delete toaster visible!"
        assert product_text != self.wait_for_element(product_page_locators.in_wishlist_product_text).text, \
            "Product is visible!"