# (c) @AbirHasan2005

import os

class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = int(os.environ.get("UPDATES_CHANNEL"))
	LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
	ABOUT_BOT_TEXT = f"""
Yo! I'm simple File Store Bot!
Send me any file I will save it in my Database. Also works for channel 😌️. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Permanent File Store Nexa](https://t.me/{BOT_USERNAME})

🔰️ **Developer:** **@NexaBotsUpdates** and **@Nexa_bots**

👥 **Support Group:** [Nexa Bots](https://t.me/Nexa_bots)

📢 **Updates Channel:** [Nexa Bots Updates](https://t.me/NexaBotsUpdates)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** **@NexaBotsUpdates** 😳

Developer is Super **NOOB**! He is Trying to learn something New! While providing Some **FREE** bot services for You Guys ❤️! So please **DONATE** for keep this service alive ❤️!

[Donate Now](https://t.me/torrentolol/18) ❤️😌
"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is **Perment File Store Nexa Bot**.

Send me any file and I will give you a **Permanent , Sharable Link**. I Support Channel Also 😌️! Check **About Bot** Button.

Made with ❤️ by **@NexaBotsUpdates**
"""
