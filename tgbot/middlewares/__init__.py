from aiogram import Dispatcher

from tgbot.middlewares.middleware_throttling import ThrottlingMiddleware


def register_all_middlewares(dp: Dispatcher):
    dp.message.middleware(ThrottlingMiddleware())
    dp.callback_query.middleware(ThrottlingMiddleware())
