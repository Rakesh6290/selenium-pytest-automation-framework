from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):

    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    PAGE_TITLE = (By.CLASS_NAME, "title")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def add_product_to_cart(self, product_name):

        add_button = (
            By.XPATH,
            f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button[contains(text(),'Add to cart')]"
        )

        self.click_element(add_button)

    def remove_product_from_cart(self, product_name):

        remove_button = (
            By.XPATH,
            f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button[contains(text(),'Remove')]"
        )

        self.click_element(remove_button)

    def open_cart(self):

        self.click_element(self.CART_ICON)

    def get_cart_count(self):

        return self.get_element_text(self.CART_BADGE)

    def get_page_title(self):

        return self.get_element_text(self.PAGE_TITLE)

    def is_product_displayed(self, product_name):

        product = (
            By.XPATH,
            f"//div[text()='{product_name}']"
        )

        return self.find_element(product).is_displayed()
    
    def sort_products(self, sort_type):

        dropdown = Select(
            self.find_element(self.SORT_DROPDOWN)
        )

        dropdown.select_by_value(sort_type)
    
    def logout(self):

        self.click_element(self.MENU_BUTTON)

        logout_button = self.wait.until(
            EC.element_to_be_clickable(
            self.LOGOUT_LINK
            )
        )

        logout_button.click()