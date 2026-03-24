from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.keyboards.main_menu import main_menu_kb

router = Router()


@router.message(Command("cancel"))
async def cmd_cancel(message: Message, state: FSMContext) -> None:
    current = await state.get_state()
    if current is None:
        await message.answer("Нечего отменять, ты и так в главном меню.", reply_markup=main_menu_kb())
        return
    await state.clear()
    await message.answer("Действие отменено. Чем займёмся?", reply_markup=main_menu_kb())


@router.message()
async def fallback(message: Message) -> None:
    await message.answer(
        "Я пока не понимаю произвольный текст 🤔\n"
        "Воспользуйся меню или отправь /start.",
        reply_markup=main_menu_kb(),
    )
