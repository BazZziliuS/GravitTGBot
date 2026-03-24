from aiogram import Dispatcher, F

from tgbot.routers import main_start, main_missed
from tgbot.routers.user import user_tasks, user_weather


def register_all_routers(dp: Dispatcher):
    for r in (main_start.router, user_tasks.router, user_weather.router, main_missed.router):
        r.message.filter(F.chat.type == "private")
        r.callback_query.filter(F.message.chat.type == "private")

    dp.include_router(main_start.router)
    dp.include_router(user_tasks.router)
    dp.include_router(user_weather.router)
    dp.include_router(main_missed.router)
