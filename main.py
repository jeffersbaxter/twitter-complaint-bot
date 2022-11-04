from time import sleep

from internet_speed_bot import InternetSpeedBot
from twitter_bot import TwitterBot

PROMISED_DOWN = 150
PROMISED_UP = 10

isp_bot = InternetSpeedBot()
# twitter_bot = TwitterBot()
sleep(10)
isp_bot.get_internet_speed()
# twitter_bot.tweet_at_provider()

sleep(30)
print(isp_bot.down)
print(isp_bot.up)

isp_bot.driver.quit()
