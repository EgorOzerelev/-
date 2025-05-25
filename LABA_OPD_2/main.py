from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties
import asyncio

API_TOKEN = "7640627366:AAEIjE2MVXqVbLi9Y2TdnWR1ymQ1oyxr62o"

# Пример базы данных студентов
students_data = {
    "Иванов Иван": {"attendance": "90%", "score": 85},
    "Петров Петр": {"attendance": "80%", "score": 74},
    "Сидоров Сидор": {"attendance": "95%", "score": 91}
}

# Создаем бота с правильными параметрами
bot = Bot(
    token=API_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

@dp.message(F.text.in_(['/start', '/help']))
async def start_handler(message: Message):
    student_list = "\n".join(students_data.keys())
    await message.answer(
        f"Привет! Я бот по дисциплине.\nВыбери своё имя из списка:\n{student_list}\n\n"
        "Напиши своё имя точно, как в списке."
    )

@dp.message()
async def student_info(message: Message):
    name = message.text.strip()
    if name in students_data:
        data = students_data[name]
        await message.answer(
            f"Информация для <b>{name}</b>:\n📅 Посещаемость: {data['attendance']}\n📝 Баллы: {data['score']}"
        )
    else:
        await message.answer("Имя не найдено. Пожалуйста, проверь написание.")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())