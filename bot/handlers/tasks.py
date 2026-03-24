from aiogram import F, Router
from aiogram.filters import Command, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message

from bot.db.models import add_task, complete_task, get_active_tasks
from bot.keyboards.main_menu import main_menu_kb, tasks_inline_kb

router = Router()


class AddTaskStates(StatesGroup):
    waiting_for_text = State()


@router.message(Command("done"))
async def cmd_done(message: Message, command: CommandObject) -> None:
    if not command.args:
        await message.answer("Укажи номер задачи: /done 1")
        return

    tasks = await get_active_tasks(message.from_user.id)
    if not tasks:
        await message.answer("Список задач пуст.")
        return

    try:
        idx = int(command.args)
    except ValueError:
        await message.answer("Номер задачи должен быть числом.")
        return

    if idx < 1 or idx > len(tasks):
        await message.answer(f"Нет задачи с номером {idx}. Всего задач: {len(tasks)}.")
        return

    task_id = tasks[idx - 1][0]
    await complete_task(task_id, message.from_user.id)
    await message.answer(f"Задача \"{tasks[idx - 1][1]}\" выполнена! 🎉")


@router.message(F.text == "📋 Мои задачи")
async def show_tasks(message: Message) -> None:
    tasks = await get_active_tasks(message.from_user.id)
    if not tasks:
        await message.answer("У тебя пока нет задач. Самое время добавить! 🎉")
        return
    await message.answer(
        "Твои текущие задачи (нажми ✅, чтобы завершить):",
        reply_markup=tasks_inline_kb(tasks, page=0),
    )


@router.callback_query(F.data.startswith("page:"))
async def paginate_tasks(callback: CallbackQuery) -> None:
    page = int(callback.data.split(":")[1])
    tasks = await get_active_tasks(callback.from_user.id)
    if not tasks:
        await callback.message.edit_text("Все задачи выполнены! 🎉")
        return
    await callback.message.edit_reply_markup(reply_markup=tasks_inline_kb(tasks, page=page))
    await callback.answer()


@router.callback_query(F.data == "noop")
async def noop_callback(callback: CallbackQuery) -> None:
    await callback.answer()


@router.message(F.text == "➕ Новая задача")
async def new_task_prompt(message: Message, state: FSMContext) -> None:
    await state.set_state(AddTaskStates.waiting_for_text)
    await message.answer(
        "Напиши текст задачи, и я её сохраню.\n"
        "Или отправь /cancel, чтобы отменить."
    )


@router.message(AddTaskStates.waiting_for_text)
async def save_task(message: Message, state: FSMContext) -> None:
    text = message.text
    if not text or text.startswith("/"):
        await state.clear()
        await message.answer("Добавление задачи отменено.", reply_markup=main_menu_kb())
        return
    await add_task(message.from_user.id, text)
    await state.clear()
    await message.answer("✅ Задача добавлена!", reply_markup=main_menu_kb())


@router.callback_query(F.data.startswith("done:"))
async def mark_done(callback: CallbackQuery) -> None:
    parts = callback.data.split(":")
    task_id = int(parts[1])
    page = int(parts[2]) if len(parts) > 2 else 0

    success = await complete_task(task_id, callback.from_user.id)
    if success:
        await callback.answer("Задача выполнена! 🎉")
    else:
        await callback.answer("Задача не найдена или уже выполнена.")

    tasks = await get_active_tasks(callback.from_user.id)
    if tasks:
        await callback.message.edit_text(
            "Твои текущие задачи (нажми ✅, чтобы завершить):",
            reply_markup=tasks_inline_kb(tasks, page=page),
        )
    else:
        await callback.message.edit_text("Все задачи выполнены! 🎉")
