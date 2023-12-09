import logging, asyncio, nekos, random
from aiogram import Bot, Dispatcher, executor, types
from configure import TOKEN, sticker

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

keyboard = types.InlineKeyboardMarkup(row_width=3)
keyboard.add(types.InlineKeyboardButton(text='🐱 неко❤', callback_data='neko'), types.InlineKeyboardButton(text='💋 поцелуй', callback_data='kiss'))
keyboard.add(types.InlineKeyboardButton(text='🐱 неко гифкой', callback_data='neko_gif'), types.InlineKeyboardButton(text='🤗 объятия', callback_data='hug_gif'))
keyboard.add(types.InlineKeyboardButton(text='🌌 обои', callback_data='wallpaper'), types.InlineKeyboardButton(text='🎆 аватарка', callback_data='avatar'))

@dp.message_handler(commands=['start'])
async def command_handler(message: types.Message):
    await message.answer_sticker(sticker=sticker)
    eji = ['😋', '🤗', '🥺', '🥰', '😍']
    emoji =  random.choice(eji)
    await message.answer(f"{emoji} просто нажми👇", reply_markup=keyboard, parse_mode='html')

@dp.callback_query_handler(lambda c: c.data == "neko")
async def neko(callback_query: types.CallbackQuery):
    eji = ['😋', '🤗', '🥺', '🥰', '😍']
    emoji =  random.choice(eji)
    await bot.send_photo(callback_query.message.chat.id, nekos.img('neko'), reply_markup=keyboard)
    await bot.answer_callback_query(callback_query.id, show_alert=False, text=f"{emoji})")

@dp.callback_query_handler(lambda c: c.data == "kiss")
async def kiss(callback_query: types.CallbackQuery):
    eji = ['😋', '🤗', '🥺', '🥰', '😍']
    emoji =  random.choice(eji)
    await bot.send_video(callback_query.message.chat.id, nekos.img('kiss'), reply_markup=keyboard)
    await bot.answer_callback_query(callback_query.id, show_alert=False, text=f"{emoji} )")

@dp.callback_query_handler(lambda c: c.data == "neko_gif")
async def neko_gif(callback_query: types.CallbackQuery):
    eji = ['😋', '🤗', '🥺', '🥰', '😍']
    emoji =  random.choice(eji)
    await bot.send_video(callback_query.message.chat.id, nekos.img('ngif'), reply_markup=keyboard)
    await bot.answer_callback_query(callback_query.id, show_alert=False, text=f"{emoji})")

@dp.callback_query_handler(lambda c: c.data == "hug_gif")
async def hug_gif(callback_query: types.CallbackQuery):
    eji = ['😋', '🤗', '🥺', '🥰', '😍']
    emoji =  random.choice(eji)
    await bot.send_video(callback_query.message.chat.id, nekos.img('hug'), reply_markup=keyboard)
    await bot.answer_callback_query(callback_query.id, show_alert=False, text=f"{emoji})")

@dp.callback_query_handler(lambda c: c.data == "wallpaper")
async def wallpaper(callback_query: types.CallbackQuery):
    eji = ['😋', '🤗', '🥺', '🥰', '😍']
    emoji =  random.choice(eji)
    await bot.send_photo(callback_query.message.chat.id, nekos.img('wallpaper'), reply_markup=keyboard)
    await bot.answer_callback_query(callback_query.id, show_alert=False, text=f"{emoji})")

@dp.callback_query_handler(lambda c: c.data == "avatar")
async def avatar(callback_query: types.CallbackQuery):
    eji = ['😋', '🤗', '🥺', '🥰', '😍']
    emoji =  random.choice(eji)
    await bot.send_photo(callback_query.message.chat.id, nekos.img('avatar'), reply_markup=keyboard)
    await bot.answer_callback_query(callback_query.id, show_alert=False, text=f"{emoji})")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

