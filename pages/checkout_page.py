from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):

    FIRSTNAME_INPUT = (By.ID, "first-name")
    LASTNAME_INPUT = (By.ID, "last-name")
    ZIPCODE_INPUT = (By.ID, "postal-code")

    CONTINUE_BUTTON = (By.ID, "continue")

    FINISH_BUTTON = (By.ID, "finish")

    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")

    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def enter_checkout_details(
        self,
        first_name,
        last_name,
        zip_code
    ):

        self.enter_text(
            self.FIRSTNAME_INPUT,
            first_name
        )

        self.enter_text(
            self.LASTNAME_INPUT,
            last_name
        )

        self.enter_text(
            self.ZIPCODE_INPUT,
            zip_code
        )

    def click_continue(self):

        self.click_element(
            self.CONTINUE_BUTTON
        )

    def click_finish(self):

        self.click_element(
            self.FINISH_BUTTON
        )

    def get_success_message(self):

        return self.get_element_text(
            self.SUCCESS_MESSAGE
        )

    def get_error_message(self):

        return self.get_element_text(
            self.ERROR_MESSAGE
        )