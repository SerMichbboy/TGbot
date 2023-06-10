import time

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from qwe import get_text, add_brat
from BTCUSDT import return_price
from Seer import read
import random
import datetime


TOKEN = "6109198023:AAFpGVo-FFNeY2l4JvreXrNgnsx249wmli4"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
keyboard = types.ReplyKeyboardMarkup(keyboard=[
        [types.KeyboardButton(text='Дай цитату, брат')],
        [types.KeyboardButton(text='Сколько время, брат?')],
        [types.KeyboardButton(text='По чём биток, брат?!')],
        [types.KeyboardButton(text='Посоветуй, брат!')],
        [types.KeyboardButton(text='Битва - молитва!')]])


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.Message):
    await msg.answer(
        f'Какими ветерками тебя занесло {msg.from_user.first_name}? '
        f'Выкладывай давай, чего хочешь?', reply_markup=keyboard)


@dp.message_handler(regexp='Битва ебланов')
async def send_welcome(msg: types.Message):
    await msg.answer(
        f'Пока не реализовано', reply_markup=keyboard)


@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
    if msg.text.lower() == 'привет':
        await msg.answer('Дарова, заэбал!')
    elif msg.text == 'Дай цитату, брат':
        await msg.answer(random.choice(add_brat(get_text('Citates_list.txt'))), reply_markup=keyboard)
    elif msg.text == 'По чём биток, брат?!':
        await msg.answer(f'По {return_price()}, брат!')
    elif msg.text == 'Посоветуй, брат!':
        await msg.answer('Задавай вопрос, брат!')

        time.sleep(15)
        await msg.answer(read(), reply_markup=keyboard)
    elif msg.text == 'Сколько время, брат?':
        d = datetime.datetime.now()
        await msg.answer(f"Щас скажу...")
        time.sleep(1)
        await msg.answer(f"{d.strftime('%H:%M')} и {d.strftime('%S')} секи, брат!", reply_markup=keyboard)
    else:
        await msg.answer("казахстан, брат!", reply_markup=keyboard)


if __name__ == '__main__':
    executor.start_polling(dp)
