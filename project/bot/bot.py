import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hbold, hlink
from project.parser.parser import get_data
from config import BOT_TOKEN
import json
import time

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_cmd(message:types.Message):
    await message.answer('Введите название товара')

@dp.message_handler()
async def parse_category(message:types.Message):
    await message.answer('Идет сбор данных...')
    try:
        get_data(message.text)

    except: pass

    finally:

        with open('products.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        for index, item in enumerate(data):
            card = f'{hlink(item.get("goods_name"), item.get("link"))}\n' \
                f'{hbold("Скидка: ")}{item.get("discount")}\n' \
                f'{hbold("Минимальная цена: ")}{item.get("lower_price")}\n' \
                f'{hbold("Старая цена: ")}{item.get("old_price")}\n' \
                f'{hbold(item.get("image"))}\n' \
            

            if index%20 == 0:
                time.sleep(3)
            await message.answer(card)
        

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
