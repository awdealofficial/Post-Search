# (c) @RoyalKrrishna

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", "9411723"))
    API_HASH = os.environ.get("API_HASH", "30fa091455c0548d77dc254f0bb705b0")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5496693865:AAEsyCi-tFpsDID-0X0zFrZjfK_DqF-1n08")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BQCWip3iLgEZTWjjIGBKAXK4UfbQecTLwNlZKQxk8dhoi23VD3hfRm$    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001668318959"))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Mdisksearch_Tgbot")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "875770605"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is Mdisk Search Bot.

 ^= ^v My Name: <a href='https://t.me/Hollywood_in_HindiHD'>Mdisk Search Robot</a>

 ^=^s^} Language : <a href='https://www.python.org'> Python V3</a>

 ^=^s^z Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

 ^=^s  Server: <a href='https://heroku.com'>Heroku</a>
