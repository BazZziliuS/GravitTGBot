import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from tgbot.data.config import BOT_TOKEN
from tgbot.database.db_helper import database_init, database_close
from tgbot.middlewares import register_all_middlewares
from tgbot.routers import register_all_routers


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    if not BOT_TOKEN:
        raise SystemExit("BOT_TOKEN не задан. Создайте файл .env с переменной BOT_TOKEN.")

    await database_init()

    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    register_all_middlewares(dp)
    register_all_routers(dp)

    logging.info("Бот запущен")
    try:
        await dp.start_polling(bot)
    finally:
        await database_close()
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.warning("Бот остановлен")
