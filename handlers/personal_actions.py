import os

from aiogram import types, dispatcher, Bot
from dispatcher import dp, bot
from aiogram.dispatcher import FSMContext
from analitic import ASD
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from langdetect import detect
from pytickersymbols import PyTickerSymbols
import investpy
import numpy as np
from datetime import date
import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


from bot import BotDB


inline_btn_1 = InlineKeyboardButton('Аналитика акций', callback_data='button1')
inline_btn_2 = InlineKeyboardButton('Прикол с пакетами', callback_data='button2')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2)
inline_btn_3 = InlineKeyboardButton('Анализировать следующую акцию', callback_data='button3')
inline_kb2 = InlineKeyboardMarkup().add(inline_btn_3)

class Form(StatesGroup):
    peremennaya = State()


@dp.message_handler(commands=['start'])
# user command
async def start(message: types.Message):
    await bot.send_message(message.from_user.id,
                           '🔸Приветсутвуем вас в нашем боте!\nВыберите одно из действий, которое вы хотите сделать', reply_markup=inline_kb1)


@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "🔸Введите тикер компании:")
    await Form.peremennaya.set()
@dp.callback_query_handler(lambda c: c.data == 'button3')
async def process_callback_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "🔸Введите тикер компании:")
    await Form.peremennaya.set()

@dp.callback_query_handler(lambda c: c.data == 'button2')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "— Кто проживает в закладке районной? \n— Спайс “Боб” квадратный пакет!")
@dp.message_handler(state=Form.peremennaya) # Принимаем состояние
async def peremennaya(message: types.Message, state: FSMContext):
    async with state.proxy() as a:
        a['peremennaya'] = message.text
    await state.finish()
    Spisok=[]
    try:
        Spisok = ASD.anal(a['peremennaya'])
        data = {'Цена': [Spisok[10], Spisok[11], Spisok[12], Spisok[13], Spisok[14], Spisok[15], Spisok[16], Spisok[17], Spisok[18], Spisok[19], Spisok[20], Spisok[21], Spisok[22], Spisok[23], Spisok[24]]}
        df = pd.DataFrame(data)
        x = np.arange(15)
        plt.plot(x, df)
        plt.title('Изменение цены')
        plt.xlabel('Дни')
        plt.ylabel('Цена')
        userid = message.from_user.id
        plt.legend(data)
        plt.savefig(str(userid)+'.png')
        photo = open(str(userid)+'.png', 'rb')
        plt.clf()
        await bot.send_photo(message.from_user.id, photo = photo, caption ='🔸Технический индикатор\nк покупке: '+str(Spisok[0])+' из 12   к продаже: '+str(Spisok[1])+' из 12\n🔸После иследования рейтинга SMA\n к покупке: '+str(Spisok[2])+' из 6   к продаже: '+str(Spisok[3])+' из 6\n🔸После иследования рейтинга EMA\nк покупке: '+str(Spisok[4])+' из 6    к продаже: '+str(Spisok[5])+' из 6\n▪Так же нa графике мы можем увидеть изменения стоимости за 15 дней\n▪Наш анализ и вывод по поводу этой акции вам стоит: '+str(Spisok[25]), reply_markup=inline_kb2)

    except:
            await bot.send_message(message.from_user.id,'Данного эмитента нет в базе данных')














