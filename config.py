import re

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 22731333
API_HASH = "f8f993acb1d5f51c950ba873404d9af5"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7829763759:AAGybodD0whDeBYqyzLkrVEt9rcO3xkzKgM"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://I-LOVE-PDF-BOT:I-LOVE-PDF-BOT@cluster0.c51o3a9.mongodb.net/?retryWrites=true&w=majority"
MUSIC_BOT_NAME = "@One_for_all_rebot"
PRIVATE_BOT_MODE = None

DURATION_LIMIT_MIN = 900

# Chat id of a group for logging bot's activities
LOGGER_ID = "-1002009280180"

# Get this value from @One_for_all_rebot on Telegram by /id
OWNER_ID = 7078181502

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = ""
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = "HRKU-ebe35615-918a-473e-8474-d9eb2e506391"

UPSTREAM_REPO = "https://github.com/Gokukhan1/musicgoku"

UPSTREAM_BRANCH = "main"
GIT_TOKEN = None  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/PiratesBotRepo"
SUPPORT_CHAT = "https://t.me/PiratesMainchat"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = False

# Auto Gcast/Broadcast Handler (True = broadcast on , False = broadcast off During Hosting, Dont Do anything here.)
AUTO_GCAST = False

# Auto Broadcast Message That You Want Use In Auto Broadcast In All Groups.
AUTO_GCAST_MSG = ""

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = "bcfe26b0ebc3428882a0b5fb3e872473"
SPOTIFY_CLIENT_SECRET = "907c6a054c214005aeae1fd752273cc4"


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
SERVER_PLAYLIST_LIMIT = "50"
PLAYLIST_FETCH_LIMIT = "25"

SONG_DOWNLOAD_DURATION = "180"
SONG_DOWNLOAD_DURATION_LIMIT = "2000"

# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = 104857600
TG_VIDEO_FILESIZE_LIMIT = 1073741824
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @BRANDEDSTRINGSESSION_BOT on Telegram
STRING1 = "BQFa2kUAXRWdweRFofJ7GR9xJ1ECkaHFzhOwL7xdYdZloLC_MDG66_xYJR1FlK59sjsb9feC0iKwFpNeLl8UTPL8MO8MOcRvUPoRr330V2yb1FlhvS8ns-si0qkrrMnWb1L_M0HVobBGflsv7E8gcFzZY6gmrHGNOrTFkd475vWS9yXgzcf2ia6EYliLwKjCVf1FnrVzIQgiU1mYCLYXWb5dj9IgAtB9Y4F4dw3N2-YAhHT8eAvGIQ4VwjVKN25FrjpNtqjNKqDRxjIC6KxhSuoyEmSlZNxSjPXU1YHnuz_KY6OWPgC7yJLplZiU0kn7klrHZqHn6kBjYfRbukzJK1IFpvwTZgAAAAHfXphZAA"
STRING2 = None
STRING3 = None
STRING4 = None
STRING5 = None


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://files.catbox.moe/t0t93h.jpg"
PING_IMG_URL = "https://files.catbox.moe/lbl62s.jpg"
PLAYLIST_IMG_URL = "https://files.catbox.moe/ka4lzo.jpg"
STATS_IMG_URL = "https://files.catbox.moe/o82ph9.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/ka4lzo.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/lbl62s.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/t0t93h.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/o82ph9.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/o82ph9.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/ka4lzo.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/lbl62s.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/t0t93h.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
