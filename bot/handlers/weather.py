from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.keyboards.main_menu import main_menu_kb
from bot.services.weather import get_weather
from bot.states.weather import WeatherStates

router = Router()


@router.message(F.text == "🌤 Погода")
async def weather_prompt(message: Message, state: FSMContext) -> None:
    await state.set_state(WeatherStates.waiting_for_city)
    await message.answer(
        "Напиши название города, и я покажу текущую погоду.\n"
        "Или отправь /cancel, чтобы вернуться в меню."
    )


@router.message(WeatherStates.waiting_for_city)
async def show_weather(message: Message, state: FSMContext) -> None:
    city = message.text
    if not city or city.startswith("/"):
        await state.clear()
        await message.answer("Отменено.", reply_markup=main_menu_kb())
        return

    result = await get_weather(city)
    await state.clear()

    if result:
        await message.answer(f"🌤 {result}", reply_markup=main_menu_kb())
    else:
        await message.answer(
            "Не удалось найти погоду для этого города. 😕\n"
            "Проверь название и попробуй ещё раз.",
            reply_markup=main_menu_kb(),
        )
