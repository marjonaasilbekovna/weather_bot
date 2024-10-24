import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from weather import weather
from inline_button import menu, menu_country, sozlama
from state import Vaqt
import time

TOKEN = "7270059308:AAFSm22a8TtM75alFQBQSAXMBxgwIDikIK4"
ADMIN_ID = [5012784380]

dp = Dispatcher()

@dp.message(Command("start"))
async def command_start_handler(message: Message, state:FSMContext):
    full_name = message.from_user.full_name
    text = f"Assalomu alaykum {full_name}, Ob-havo botiga hush kelibsiz"
    
    await message.answer(text)
    await message.answer("Ob-havo malumotlarini olish uchun siz yashaydigan shahar yoki tuman nomini tugmalardan tanlang", reply_markup=menu)

# foydalanuvchi tanlagan shahar haqida malumot chiqarish
@dp.callback_query(lambda callback_query: callback_query.data in menu_country.keys())
async def weather_info(callback_query: CallbackQuery, state:FSMContext):
    selected_city = callback_query.data
    ob_havo_info = weather(selected_city)
    
    await callback_query.message.answer(f"{menu_country[selected_city]} shahridagi ob-havo ma'lumotlari:\n\n{ob_havo_info}", reply_markup=sozlama)
    
    await callback_query.message.delete()

@dp.callback_query(F.data=="change")
async def change_code(callback_query:CallbackQuery):
    await callback_query.message.answer("Shaqxar dan birini tanlang", reply_markup=menu)
    
@dp.message(F.text=="Add")
async def add_timer(message: Message, state:FSMContext):
    await message.answer("Vaqtni kiriting !")
    await state.set_state(Vaqt.vaqt)

@dp.message(Vaqt.vaqt)
async def timer(message: Message, state:FSMContext):
    text = message.text

    while True:
        if time.strftime('%Y-%m-%d %H:%M:%S') == text:
            await message.answer("Its time")
            # break
        else:
            continue
    
    await state.clear()

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


