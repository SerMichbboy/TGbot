from aiogram import Bot, Dispatcher, executor, types

TOKEN = "6109198023:AAFpGVo-FFNeY2l4JvreXrNgnsx249wmli4"

bot = Bot(TOKEN)
dp = Dispatcher(bot)

keyboard = types.ReplyKeyboardMarkup(keyboard=[
    [types.KeyboardButton(text='Дай цитату, брат')],
    [types.KeyboardButton(text='Сколько время, брат?')],
    [types.KeyboardButton(text='По чём биток, брат?!')],
    [types.KeyboardButton(text='Посоветуй, брат!')],
    [types.KeyboardButton(text='Битва - молитва!')],
    [types.KeyboardButton(text='Дай волка, Брат')]])


if __name__ == "__main__":
    executor.start_polling(dp)



