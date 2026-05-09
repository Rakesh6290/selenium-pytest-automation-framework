from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)


    # =========================
       # ELEMENT ACTIONS
    # =========================
    def find_element(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def click_element(self, locator):
        self.find_element(locator).click()

    def get_element_text(self, locator):
        return self.find_element(locator).text
    
  