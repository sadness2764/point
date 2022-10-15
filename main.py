from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
import os
from dotenv import load_dotenv
from keyboards import *

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def first(message: Message):
    await message.answer(f'''Так стоп а ты откуда пришел а ну иди нахер.                       
Эй постойка тебя вроде в тг ник {message.from_user.username}
Так вот чо иди нахер {message.from_user.username}
А еще кое-что если будешь пиздеть всем подрять про меня то я тебя найду
У меня твой id
ХхаХАХахАХАХХАХАХАХАА
Если не веришь то вот: {message.from_user.id}
хАХХАхахАХА лох''', reply_markup=first_keyboards())


@dp.message_handler(regexp=r'Нажми')
async def two(message: Message):
    await message.answer(f'''Ты нахуя нажал''', reply_markup=two_keyboards())


@dp.message_handler(regexp=r'Если нажмешь то я узнаю твой номер')
async def tree(message: Message):
    await message.answer(f'''Ты сука напросился
У меня твой номер хахаха
Тебя пизда''', reply_markup=tree_keyboards())


@dp.message_handler(regexp=r'Только посмей сука нажать эту кнопку')
async def four(message: Message):
    await message.answer(f'''Ну хорошо ты не нажимаешь эту кнопу а я не буду обращаться стобой как собакой''',
                         reply_markup=four_keyboards())


@dp.message_handler(regexp=r'...')
async def five(message: Message):
    await message.answer(f'''Короче я и так слаб нехочу портить всое время поэтому пока''',
                         reply_markup=five_keyboards())


@dp.message_handler(regexp=r'Пока')
async def six(message: Message):
    await message.answer(f'''👋''')


@dp.message_handler(regexp=r'Иди нахуй')
async def seven(message: Message):
    await message.answer(f'''👌👍''')


executor.start_polling(dp)
