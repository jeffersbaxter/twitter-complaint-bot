from time import sleep
from selenium_bot import SeleniumBot
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException


class InternetSpeedBot(SeleniumBot):
    def __init__(self):
        super().__init__("https://www.speedtest.net/")
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        go = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go.click()
        while True:
            try:
                modal = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/a')
                modal.click()
            except ElementNotInteractableException:
                sleep(5)
                continue
            else:
                sleep(2)
                self.down = float(self.driver.find_element(By.CSS_SELECTOR, "span.download-speed").text)
                self.up = float(self.driver.find_element(By.CSS_SELECTOR, "span.upload-speed").text)
                break

