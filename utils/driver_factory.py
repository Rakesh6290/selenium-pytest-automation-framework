from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService


def get_driver(browser="chrome"):

    if browser.lower() == "chrome":

        driver = webdriver.Chrome(
            service=ChromeService(
                r"C:\drivers\chromedriver.exe"
            )
        )

    elif browser.lower() == "firefox":

        driver = webdriver.Firefox(
            service=FirefoxService(
                r"C:\drivers\geckodriver.exe"
            )
        )

    elif browser.lower() == "edge":

        driver = webdriver.Edge(
            service=EdgeService(
                r"C:\drivers\msedgedriver.exe"
            )
        )

    else:

        raise Exception(
            f"Browser '{browser}' not supported."
        )

    driver.maximize_window()
   
    return driver                  