import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
PATH_DATABASE = os.getenv("DB_PATH", "tgbot/data/database.db")
