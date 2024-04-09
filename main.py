import aiogram
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
import asyncio
import nest_asyncio

API_TOKEN = "6135619688:AAFZXb9PfZgyLoScaU5psbBCDQIKXcBwrH8"
BOT = Bot(token = API_TOKEN)
DP = Dispatcher()

@DP.message(Command("start"))
async def cmd_start(message: types.Message):
    button = types.KeyboardButton(text='Кто?')
    button2 = types.KeyboardButton(text='Куда?')
    kb = types.ReplyKeyboardMarkup(keyboard=[[button, button2]],
                                   one_time_keyboard=True)
    await message.answer('Привет!', reply_markup=kb)


@DP.message(F.text == 'Кто?')
async def cmd_who(message: types.Message):
    await message.answer('Где?')

@DP.message(F.text == 'Куда?')
async def cmd_where(message: types.Message):
    await message.answer('Зачем?', reply_markup=types.ReplyKeyboardRemove())

    kb = InlineKeyboardBuilder()
    button = types.InlineKeyboardButton(text="В меню", callback_data="В меню")

    kb.row(button)
    await message.answer('Желаете вернуться в меню?',
                         reply_markup=kb.as_markup())

@DP.callback_query(F.data == "В меню")
async def cb_menu(callback: types.CallbackQuery):
    await callback.message.answer('А у нас его нет')
    await callback.answer()

@DP.message()
async def cmd_echo(message: types.Message):
    await message.answer(message.text)

async def main():
    await DP.start_polling(BOT)

nest_asyncio.apply()
asyncio.run(main())
