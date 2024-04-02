from extra import internet_speed_bot

bot = internet_speed_bot()
# data = bot.get_internet_speed()
data = ["23.09", "9.16", "BSNL"]
bot.tweet_at_provider(data)
# bot.tweet_at_provider()
