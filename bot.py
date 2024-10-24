import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from weather import weather
from inline_button import menu, menu_country
from state import Shahar

TOKEN = "7181305178:AAEVp764bS7csy8A7lcAXUrNkj7Z9x--2hE"
ADMIN_ID = [7241341727]

dp = Dispatcher()

@dp.message(Command("start"))
async def command_start_handler(message: Message, state:FSMContext):
    full_name = message.from_user.full_name
    text = f"Assalomu alaykum {full_name}, Ob-havo botiga hush kelibsiz"
    
    await message.answer(text)
    await message.answer("Ob-havo malumotlarini olish uchun siz yashaydigan shahar yoki tuman nomini tugmalardan tanlang", reply_markup=menu)
    await state.set_state(Shahar.shahar1)

# foydalanuvchi tanlagan shahar haqida malumot chiqarish
@dp.callback_query(lambda callback_query: callback_query.data in menu_country.keys(), Shahar.shahar1)
async def weather_info(callback_query: CallbackQuery, state:FSMContext):
    selected_city = callback_query.data
    await state.update_data(city1 = shahar1)
    ob_havo_info = weather(selected_city)
    
    await callback_query.message.answer(f"{menu_country[selected_city]} shahridagi ob-havo ma'lumotlari:\n\n{ob_havo_info}")
    await callback_query.message.answer("Yana birorta shahar ob-havosi haqida malumot olmoqchimisiz?")
    await callback_query.answer() 
    state.message.delete()



@dp.startup()
async def bot_start():
    for admin in ADMIN_ID:
        await bot.send_message(admin, "Tabriklaymiz 🎉 \nBotimiz ishga tushdi ")

@dp.shutdown()
async def bot_start():
    for admin in ADMIN_ID:
        await bot.send_message(admin, "Bot to'xtadi ❗️")


async def main():
    global bot
    bot = Bot(TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


