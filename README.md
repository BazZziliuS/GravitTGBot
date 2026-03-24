# Личный ассистент задач | Telegram Bot

Telegram-бот для управления списком задач с интеграцией погодного API.

## Функционал

- **Управление задачами** - добавление, просмотр и завершение задач через удобные кнопки
- **Персистентность** - задачи хранятся в SQLite и сохраняются между перезапусками
- **Погода** - текущая погода по названию города (wttr.in)
- **FSM-диалоги** - ввод задач и города через машину состояний aiogram

## Запуск

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/BazZziliuS/GravitTGBot.git
cd GravitTGBot
```

### 2. Установите зависимости

```bash
uv sync
```

### 3. Создайте файл `.env`

```bash
cp .env.example .env
```

Откройте `.env` и вставьте токен вашего бота, полученный у [@BotFather](https://t.me/BotFather):

```
BOT_TOKEN=123456:ABC-DEF...
```

### 4. Запустите бота

```bash
uv run python main.py
```

_Лучший темплейт: https://github.com/djimboy/djimbo_template_aio3_