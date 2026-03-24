from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.keyboards.main_menu import main_menu_kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    name = message.from_user.first_name or "друг"
    await message.answer(
        f"Привет, {name}! 👋\n\n"
        "Я твой личный ассистент задач.\n"
        "Добавляй задачи, отслеживай их и узнавай погоду, всё в одном месте.\n\n"
        "Выбери действие в меню ниже:",
        reply_markup=main_menu_kb(),
    )
