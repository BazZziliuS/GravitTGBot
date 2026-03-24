from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from tgbot.keyboards.reply_main import main_menu_kb

router = Router(name=__name__)


@router.message(Command("cancel"))
async def cmd_cancel(message: Message, state: FSMContext):
    current = await state.get_state()
    if not current:
        await message.answer("Нечего отменять, ты и так в главном меню.", reply_markup=main_menu_kb())
        return
    await state.clear()
    await message.answer("Действие отменено. Чем займёмся?", reply_markup=main_menu_kb())


@router.message()
async def fallback(message: Message):
    await message.answer(
        "Я пока не понимаю произвольный текст 🤔\n"
        "Воспользуйся меню или отправь /start.",
        reply_markup=main_menu_kb(),
    )
