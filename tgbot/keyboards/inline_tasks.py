from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

TASKS_PER_PAGE = 5


def tasks_inline_kb(tasks: list[tuple[int, str]], page: int = 0) -> InlineKeyboardMarkup:
    total = len(tasks)
    total_pages = max(1, (total + TASKS_PER_PAGE - 1) // TASKS_PER_PAGE)
    page = max(0, min(page, total_pages - 1))

    start = page * TASKS_PER_PAGE
    end = start + TASKS_PER_PAGE
    page_tasks = tasks[start:end]

    buttons = []
    for idx, (task_id, text) in enumerate(page_tasks, start=start + 1):
        short = text if len(text) <= 40 else text[:37] + "..."
        buttons.append(
            [InlineKeyboardButton(
                text=f"{idx}. {short}  ✅",
                callback_data=f"done:{task_id}:{page}",
            )]
        )

    if total_pages > 1:
        nav = []
        if page > 0:
            nav.append(InlineKeyboardButton(text="⬅️", callback_data=f"page:{page - 1}"))
        nav.append(InlineKeyboardButton(text=f"{page + 1}/{total_pages}", callback_data="noop"))
        if page < total_pages - 1:
            nav.append(InlineKeyboardButton(text="➡️", callback_data=f"page:{page + 1}"))
        buttons.append(nav)

    return InlineKeyboardMarkup(inline_keyboard=buttons)
