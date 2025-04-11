from selenium.webdriver.common.by import By


class parameters:
    website_link = "https://www.amazon.com"
    email = "oguz.celik@useinsider.com"
    password = "Test123!"
    search_text = "samsung"


class login_page_locators:
    navigate_login_page = (By.CLASS_NAME, "nav-line-1-container")
    email = (By.NAME, "email")
    login_email = (By.ID, "continue")
    password = (By.ID, "ap_password")
    login = (By.ID, "signInSubmit")


class search_page_locators:
    search_textbox = (By.ID, "twotabsearchtextbox")
    search = (By.ID, "nav-search-submit-button")
    second_page = (By.CLASS_NAME, "a-last")
    product = (By.XPATH, "((//div[@data-index = 2])[1]//a)[1]")


class product_page_locators:
    add_to_wishlist = (By.ID, "add-to-wishlist-button-submit")
    product_text = (By.XPATH, "//span[@class = 'huc-atwl-header-small']")
    in_wishlist_product_text = (By.CSS_SELECTOR, ".a-size-small .a-size-base .a-link-normal ")
    wishlist = (By.ID, "huc-view-your-list-button")
    delete = (By.CSS_SELECTOR, "[name='submit.deleteItem']")
    deleted_text = (By.XPATH, "//div[@class = 'a-alert-content' and text()='Deleted']")