from aiogram.utils.keyboard import ReplyKeyboardBuilder


def main_menu_kb():
    kb = ReplyKeyboardBuilder()
    kb.button(text="📋 Мои задачи")
    kb.button(text="➕ Новая задача")
    kb.button(text="🌤 Погода")
    kb.adjust(2, 1)
    return kb.as_markup(resize_keyboard=True)