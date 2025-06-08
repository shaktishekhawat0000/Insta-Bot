from instabot import Bot

bot = Bot()

bot.login(username="kuma.rsanum", password="kamikaze2")

bot.follow("jasleenroyal")

bot.upload_photo("C:\Users\shakt\OneDrive\Desktop\Practice\uploadit.jpg")

bot.unfollowfollow("jasleenroyal")

bot.send_message("I love Basketball",["_pratapxsurya_"])

followers = bot.get_user_followers("kuma.rsanum")

for follower in followers:
    print(bot.get_user_info(follower))


followings = bot.get_user_following("kuma.rsanum")

for following in followings:
    print(bot.get_user_info(following))
