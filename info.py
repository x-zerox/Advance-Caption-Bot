from os import environ, getenv
import re
import os

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


ADMIN = int(getenv("ADMIN", "1923770971"))
SILICON_PIC = os.environ.get("SILICON_PIC", "https://graph.org/file/eb55d47e5e0db43ec6722-547b6b538e0ae14564.jpg")
API_ID = int(getenv("API_ID", "9328697"))
API_HASH = str(getenv("API_HASH", "9844b5bade2267c9a175a1dc72952e76"))
BOT_TOKEN = str(getenv("BOT_TOKEN", ""))
FORCE_SUB = os.environ.get("FORCE_SUB", "Ajeet_bots") 
MONGO_DB = str(getenv("MONGO_DB", "",))
DEF_CAP = str(
    getenv(
        "DEF_CAP",
        "<b>File Name:- `{file_name}`\n\n{file_size}</b>",
    )
)
