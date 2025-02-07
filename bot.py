import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.client.default import DefaultBotProperties

TOKEN = "7238271241:AAF82PYhCxoiqINJeHLJ2WfnSD895OdLL0Y"  # Вставьте сюда свой токен

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()

# 📌 /start – Приветствие и кнопка "Играть"
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🌾 Играть в ферму", web_app=types.WebAppInfo(url="https://ваша-игра.com"))]
    ])
    await message.answer("👋 Привет, фермер! Добро пожаловать в 🌾 Farm: Neighbors! \n\nЖми кнопку ниже, чтобы начать играть:", reply_markup=keyboard)

# 📌 /farm – Открытие WebApp-игры
async def open_farm(message: types.Message):
    await message.answer("🌱 Открываю твою ферму... Жми кнопку ниже!", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🌾 Перейти в игру", web_app=types.WebAppInfo(url="https://ваша-игра.com"))]
    ]))

# 📌 /market – Продажа ресурсов
async def market(message: types.Message):
    await message.answer("💰 Добро пожаловать на рынок! Пока торговля недоступна, но скоро добавим её!")

# 📌 /help – Подсказки по игре
async def help_command(message: types.Message):
    await message.answer("ℹ️ Список команд:\n"
                         "/start – Начать игру\n"
                         "/farm – Открыть ферму\n"
                         "/market – Рынок\n"
                         "/help – Помощь")

# Регистрация команд
dp.message.register(start, Command("start"))
dp.message.register(open_farm, Command("farm"))
dp.message.register(market, Command("market"))
dp.message.register(help_command, Command("help"))

# Запуск бота
async def main():
    print("🤖 Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
