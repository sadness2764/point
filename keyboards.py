from aiogram.types import KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup


def first_keyboards():
    return ReplyKeyboardMarkup([
        [KeyboardButton(text='Нажми')]
    ], resize_keyboard=True)


def two_keyboards():
    return ReplyKeyboardMarkup([
        [KeyboardButton(text='Если нажмешь то я узнаю твой номер')]
    ], resize_keyboard=True)


def tree_keyboards():
    return ReplyKeyboardMarkup([
        [KeyboardButton(text='Только посмей сука нажать эту кнопку')]
    ], resize_keyboard=True)


def four_keyboards():
    return ReplyKeyboardMarkup([
        [KeyboardButton(text='...')]
    ], resize_keyboard=True)


def five_keyboards():
    return ReplyKeyboardMarkup([
        [KeyboardButton(text='Пока'), KeyboardButton(text='Иди нахуй')]
    ], resize_keyboard=True)




