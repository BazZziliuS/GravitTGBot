from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from tgbot.keyboards.reply_main import main_menu_kb
from tgbot.services.api_weather import WTTR

router = Router(name=__name__)


class WeatherStates(StatesGroup):
    waiting_for_city = State()


@router.message(F.text == "🌤 Погода")
async def weather_prompt(message: Message, state: FSMContext):
    await state.set_state(WeatherStates.waiting_for_city)
    await message.answer(
        "Напиши название города, и я покажу текущую погоду.\n"
        "Или отправь /cancel, чтобы вернуться в меню."
    )


@router.message(WeatherStates.waiting_for_city)
async def show_weather(message: Message, state: FSMContext):
    city = message.text
    if not city or city.startswith("/"):
        await state.clear()
        await message.answer("Отменено.", reply_markup=main_menu_kb())
        return

    result = await WTTR(city).get_weather()
    await state.clear()

    if result:
        await message.answer(f"🌤 {result}", reply_markup=main_menu_kb())
    else:
        await message.answer(
            "Не удалось найти погоду для этого города. 😕\n"
            "Проверь название и попробуй ещё раз.",
            reply_markup=main_menu_kb(),
        )
