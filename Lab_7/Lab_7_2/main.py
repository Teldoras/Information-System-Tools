import asyncio
import os
import random

# import aiogram
from aiogram import Bot, types
from aiogram import Dispatcher
from aiogram import Router
from aiogram import F
from aiogram.types import FSInputFile


bot = Bot(token='') #место для телеграм-токена
dp = Dispatcher()
router = Router()


@dp.message(F.text.lower() == 'привет')
async def process_start_command(message: types.Message):
    await message.reply("Привет!")
    await give_info(message)


@dp.message(F.text.lower() == 'помощь')
async def process_help_command(message: types.Message):
    await give_info(message)


@dp.message(F.text.lower() == 'тест')
async def picture_send_command(message: types.Message):
    pic = FSInputFile((os.getcwd() + "\\сats\\" + str(random.randint(1, 3)) + ".jpg")) #путь с русскими буквами не работает
#    pic = FSInputFile("D:\\Lab_7_pics\\cats\\" + str(random.randint(1, 3)) + ".jpg")
    await bot.send_message(chat_id=message.chat.id, text="1) " + os.getcwd())
    await bot.send_message(chat_id=message.chat.id, text="2) " + str(pic.path))
    await bot.send_message(chat_id=message.chat.id, text="3) " + pic.path.strip())
#    await bot.send_message(chat_id=message.chat.id, text="4) " + "End.")
#    await bot.send_photo(chat_id=message.chat.id, photo=pic) #работает при условии пути без русских букв


@dp.message(F.text == '1')
async def picture_send_command(message: types.Message):
    pic = FSInputFile("D:\\Lab_7_pics\\cats\\" + str(random.randint(1, 3)) + ".jpg")
    await bot.send_photo(chat_id=message.chat.id, photo=pic)


@dp.message(F.text == '2')
async def picture_send_command(message: types.Message):
    pic = FSInputFile("D:\\Lab_7_pics\\dogs\\" + str(random.randint(1, 3)) + ".jpg")
    await bot.send_photo(chat_id=message.chat.id, photo=pic)


@dp.message(F.text == '3')
async def picture_send_command(message: types.Message):
    pic = FSInputFile("D:\\Lab_7_pics\\parrots\\" + str(random.randint(1, 3)) + ".jpg")
    await bot.send_photo(chat_id=message.chat.id, photo=pic)


async def give_info(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text="Я умею присылать случайные картинки из своих запасов!")
    await bot.send_message(chat_id=message.chat.id, text="У меня есть несколько картинок с милыми животными.\nВыбери категорию!")
    await bot.send_message(chat_id=message.chat.id, text="1 - Котики\n2 - Пёсики\n3 - Попугайчики")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())



