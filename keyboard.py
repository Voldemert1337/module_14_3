from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

sex_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Мужчина'),
            KeyboardButton(text='Девушка')
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [

            KeyboardButton(text='Рассчитать'),
            KeyboardButton(text='Информация'),
            KeyboardButton(text='Купить')
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)

product = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='HDD WD-Blue', callback_data='product_buying'),
            InlineKeyboardButton(text='SSD Samsung 250 gb', callback_data='product_buying'),
            InlineKeyboardButton(text='Флеш-накопитель 4gb', callback_data='product_buying'),
        ]
    ]
)
menu_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
            InlineKeyboardButton(text='Формулы расчета', callback_data='formulas')
        ]
    ]
)