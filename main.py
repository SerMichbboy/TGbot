from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from Wolves import random_wolves
from qwe import get_text, add_brat
from BTCUSDT import return_price
from Seer import read
from TKN import TOKEN

import logging
import random
import datetime
import time

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

keyboard = types.ReplyKeyboardMarkup(keyboard=[
    [types.KeyboardButton(text='Дай цитату, брат')],
    [types.KeyboardButton(text='Сколько время, брат?')],
    [types.KeyboardButton(text='По чём биток, брат?!')],
    [types.KeyboardButton(text='Посоветуй, брат!')],
    [types.KeyboardButton(text='Дай волка, Брат')]])


async def on_startup(_):
    print('Success, Brat')


HELP_COMMAND = """

<b>/help</b> - <em>оказываю помощь, брат</em>
<b>/start</b> - <em>запускаю бота, брат</em>
<b>/givemeacatbro</b> - <em>отправляю тебе котика, брат</em>

"""


@dp.message_handler(commands=['help'])
async def help_c(msg: types.Message):
    await msg.reply(text=HELP_COMMAND, parse_mode="HTML")


@dp.message_handler(commands=['givemeacatbro'])
async def give_random_cat(msg: types.Message):
    await msg.answer('<em>ДЕРЖИ!</em>', parse_mode='HTML')
    await bot.send_sticker(msg.from_user.id,
                           sticker='CAACAgIAAxkBAAEJbwlklAxseJWTp0eaOiVS_JY0G_TdfwACgwkAAvFCvwX0O30UbLbe_y8E')
    await msg.answer('<em>Для хорошего человека не жалко!</em>', parse_mode='HTML')
    await msg.delete()


@dp.message_handler(commands=['start'])
async def send_welcome(msg: types.Message):
    await msg.answer(
        f'Какими ветерками тебя занесло {msg.from_user.first_name}? '
        f' Выкладывай давай, чего хочешь?'
        f' Жми /help для просмотра твоих возможностей, Брат.', reply_markup=keyboard)


@dp.message_handler(regexp='Битва - молитва!')
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
        await msg.answer('<em>Задавай вопрос, брат, ответ на который будет Да или Нет!</em>', parse_mode='HTML')
    elif msg.text == 'Сколько время, брат?':
        d = datetime.datetime.now()
        await msg.answer(f"Щас скажу...")
        time.sleep(1)
        await msg.answer(f"{d.strftime('%H:%M')} и {d.strftime('%S')} секи, брат!", reply_markup=keyboard)
    elif msg.text == 'Дай волка, Брат':
        await msg.answer(f'Вот тебе волк, Брат! АУФ!')
        time.sleep(0.5)
        await bot.send_sticker(msg.from_user.id, sticker=random_wolves())
        await msg.delete()
    else:
        await msg.reply(f'<em>{read()}</em>', reply_markup=keyboard, parse_mode='HTML')

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
