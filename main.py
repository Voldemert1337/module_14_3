from config import *
from keyboard import *
import text
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import asyncio


bot = Bot(token=API_KEY)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    with open('i (1).webp', 'rb') as img:
        await message.answer_photo(img, "Название: SSD Samsung 250 gb|Описание: ssd накопитель Samsung на 250 гб|"
                                       "Цена:2500руб")
    with open('i (2).webp', 'rb') as img:
        await message.answer_photo(img, "Название: Флеш-накопитель 4gb|Описание: флешка на 4 гб"
                                   "|Цена:600руб")

    with open('i.webp', 'rb') as img:
        await message.answer_photo(img, "Название: HDD WD-Blue|Описание:Жесткий диск на 1т 7200 об/мин"
                                   "|Цена:5000руб")



    await message.answer("Выберите продукт для покупки:", reply_markup=product)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    print(message.text)
    await message.answer('Выберите опцию', reply_markup=menu_kb)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('Формулы расчета калорий')
    await call.message.answer('для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;')
    await call.message.answer('для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.')
    await call.answer()


@dp.message_handler(commands=['start'])
async def start(message):
    print(message.text)
    print('Привет! Я Бот помогающий твоему здоровью')
    await message.answer('Привет! Я помогаю тебе с учетом питания и здоровья', reply_markup=start_kb)


@dp.message_handler(text='Информация')
async def info(message: types.Message):
    await message.answer('Бот создан для помощи в учете питания и здоровья')
    await message.answer('Пока что вы можете рассчитать калории')


@dp.callback_query_handler(text='calories')
async def set_sex(call):

    await call.message.answer('Введите ваш пол м/ж', reply_markup=sex_kb)
    await UserState.sex.set()
    await call.answer()

@dp.message_handler(state=UserState.sex)
async def set_age(message, state):
    print(message.text)
    await state.update_data(sex_=message.text)
    await message.answer('Введите свой возраст')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    print(message.text)
    await state.update_data(age_=message.text)
    await message.answer('Введите свой рост в сантиметрах')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    print(message.text)
    await state.update_data(growth_=message.text)
    await message.answer('Введите свой вес в килограммах')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    print(message.text)
    await state.update_data(weight_=message.text)
    data = await state.get_data()
    data['growth'] = float(data.pop('growth_'))  # Convert 'growth' to integer
    data['weight'] = float(data.pop('weight_'))  # Convert 'weight' to integer
    data['age'] = float(data.pop('age_'))  # Convert 'age' to integer
    data['sex'] = data.pop('sex_')  # Update 'sex' key
    if data['sex'] == 'Мужчина':
        calories_result = 10 * data['growth'] + 6.25 * data['weight'] - 5 * data['age'] + 5
        await message.answer(f'Ваш результат в калориях: {calories_result}')
    elif data['sex'] == 'Девушка':
        calories_result = 10 * data['growth'] + 6.25 * data['weight'] - 5 * data['age'] - 161
        await message.answer(f'Ваша норма в калориях: {calories_result}')
    print(calories_result)
    await state.finish()


@dp.message_handler()
async def all_mess(message):
    print("Введите команду /start, чтобы начать общение.")
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
