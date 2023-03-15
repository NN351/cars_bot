from aiogram import types
from aiogram.dispatcher import FSMContext

from .keybords import get_menu_button, get_post_url_button # . - означает что мы импортируем файл из текущей папки
from state import CarsSearchState
from db.database import manager


# Аннотация переменных или объектов
# Сообщает к какому классу или объекту относится данная переменная
# или аргумент 

async def welcome_message(message: types.Message):
    text = "Hello, I'm bot for searching and buying cars!"
    markup = get_menu_button()
    await message.answer(text, reply_markup=markup)


async def get_categories(callback: types.CallbackQuery):
    await callback.message.answer("You pressed category button")


async def get_cars_by_name(message: types.Message):
    text = "Please send the name or model car that you want to find"
    await CarsSearchState.search_by_name.set()
    await message.answer(text)


async def search_by_name(message: types.Message, state: FSMContext):
    print(message.text)
    cars = manager.search_by_name(message.text)
    await state.finish()
    if cars:
        for car in cars:
            text = f"""
                Название: {car[1]},
                Стоимость: 
                    1) {car[2]}сом
                    2) {car[3]}$
                Номер телефона: {car[4]} 
            """
            markup =get_post_url_button(car[-1])
            await message.answer(text, reply_markup=markup)
    else:
        await message.answer("By gived name not found any cars in database")


# from parser.main import main
# import asyncio

async def update_db(message: types.Message):
    # asyncio.create_task(main())
    await message.answer("Обновление базы данных запущено успешно!")

# поиск по ценам:
async def get_by_price(message: types.Message):
    text = "Введите пожалуйста цену от которой будет производиться поиск"
    await CarsSearchState.price_start.set()
    await message.answer(text)

async def get_start_price(message: types.Message, state: FSMContext):
    start_price = message.text
    async with state.proxy() as data:
        data["start_price"] = start_price
    await CarsSearchState.price_end.set()
    await message.answer("Введите пожалуйста до какой цены будет производиться поиск")

async def get_end_price(message: types.Message, state: FSMContext):
    end_price = message.text
    start_price = 0
    async with state.proxy() as data:
        start_price = data["start_price"]
    await state.finish()
    cars = manager.search_by_price(start=start_price, end=end_price)
    print(f"{start_price}- {end_price}")
    if cars:
        for car in cars:
            text = f"""
                Название: {car[1]},
                Стоимость: 
                    1) {car[2]}сом
                    2) {car[3]}$
                Номер телефона: {car[4]} 
            """
            markup =get_post_url_button(car[-1])
            await message.answer(text, reply_markup=markup)
    else:
        await message.answer("By gived name not found any cars in database")
    


