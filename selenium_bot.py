import os

from selenium import webdriver

CHROME_DRIVER_PATH = os.environ.get("CHROME_DRIVER_PATH")


class SeleniumBot:
    def __init__(self, url: str):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.driver.get(url)
