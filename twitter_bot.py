import os

from selenium_bot import SeleniumBot
from selenium.webdriver.common.by import By

# TWITTER_USER = os.environ.get("TWITTER_USER")
# TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")


class TwitterBot(SeleniumBot):
    def __init__(self):
        super().__init__("https://www.twitter.com")

    def tweet_at_provider(self):
        pass
