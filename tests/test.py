from base.locators import parameters
from pages.loginPage import LoginFunctions
from pages.search import SearchFunctions
from pages.productPage import ProductFunctions
from selenium import webdriver
import unittest


class TestRun(unittest.TestCase):

    def setUp(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--disable-notifications')
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(parameters.website_link)
        self.login_functions = LoginFunctions(self.driver)
        self.product_functions = ProductFunctions(self.driver)
        self.search_functions = SearchFunctions(self.driver)

    def test(self):
        self.login_functions.navigate_to_login()
        self.login_functions.login()
        self.search_functions.search()
        self.search_functions.click_product()
        self.product_functions.add_to_wishlist()
        self.product_functions.navigate_to_wishlist_page()
        self.product_functions.delete_product()

    def TearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()