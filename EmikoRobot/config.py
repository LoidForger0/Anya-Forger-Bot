# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/EmikoRobot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 17789594  # integer value, dont use ""
    API_HASH = "ab1b831edb2bd32905d6572ce621f678"
    TOKEN = "5356820805:AAEH_dFyomUBBa8Kwni8s8_9zvQOZj4s1yE"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 5132611794  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "xelcius"
    SUPPORT_CHAT = "NexusXSupport"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        "-1001661365045"
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        "-1001661365045"
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgresql://ffanmravxlfbhv:94327ebc7d9b9e1dff9abce7412096a0b779b66b3e9ec8296a6cc9275ff4c447@ec2-3-222-191-168.compute-1.amazonaws.com:5432/d8q5j3e33bevos"  # needed for any database modules
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "Vc~Jfv23rh7UhAggXCldhXGsD1uWiHa~MR9JsOHQiE6Tw8qT4yjRvgB6cFNi6XAT"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = "https://t.me/xelcius"  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "G1HSYGEGCVKRX1OO"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "XJO60WA47G1L"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        ""  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = ""  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
