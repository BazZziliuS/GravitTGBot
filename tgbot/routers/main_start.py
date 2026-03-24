from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from tgbot.keyboards.reply_main import main_menu_kb

router = Router(name=__name__)


@router.message(CommandStart())
async def cmd_start(message: Message):
    first_name = message.from_user.first_name
    name = first_name if first_name not in ["", None] else "друг"
    await message.answer(
        f"Привет, {name}! 👋\n\n"
        "Я твой личный ассистент задач.\n"
        "Добавляй задачи, отслеживай их и узнавай погоду.\n\n"
        "Выбери действие в меню ниже:",
        reply_markup=main_menu_kb(),
    )
