# Личный ассистент задач | Telegram Bot

Telegram-бот для управления списком задач с интеграцией погодного API.

## Функционал

- **Управление задачами** - добавление, просмотр и завершение задач через удобные кнопки
- **Персистентность** - задачи хранятся в SQLite и сохраняются между перезапусками
- **Погода** - текущая погода по названию города (wttr.in)
- **FSM-диалоги** - ввод задач и города через машину состояний aiogram

## Стек

- Python 3.13
- [aiogram 3](https://docs.aiogram.dev/) - асинхронный фреймворк для Telegram Bot API
- aiosqlite - асинхронная работа с SQLite
- [uv](https://docs.astral.sh/uv/) - менеджер пакетов

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

## Архитектура

```
main.py                  # точка входа
bot/
  config.py              # загрузка конфигурации из .env
  db/models.py           # слой работы с SQLite
  handlers/
    start.py             # команда /start
    tasks.py             # CRUD задач + FSM
    weather.py           # погода + FSM
    common.py            # /cancel и fallback
  services/weather.py    # клиент wttr.in API
  keyboards/main_menu.py # клавиатуры
  states/weather.py      # состояния FSM для погоды
```
