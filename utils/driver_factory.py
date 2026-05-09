from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

import os


def get_driver(browser="chrome"):

    base_path = os.path.dirname(
        os.path.dirname(__file__)
    )

    if browser.lower() == "chrome":

        driver_path = os.path.join(
            base_path,
            "drivers",
            "chromedriver.exe"
        )

        driver = webdriver.Chrome(
            service=ChromeService(driver_path)
        )

    elif browser.lower() == "firefox":

        driver_path = os.path.join(
            base_path,
            "drivers",
            "geckodriver.exe"
        )

        driver = webdriver.Firefox(
            service=FirefoxService(driver_path)
        )

    elif browser.lower() == "edge":

        driver_path = os.path.join(
            base_path,
            "drivers",
            "msedgedriver.exe"
        )

        driver = webdriver.Edge(
            service=EdgeService(driver_path)
        )

    else:

        raise Exception(
            f"Browser '{browser}' not supported."
        )

    driver.maximize_window()

    return driver