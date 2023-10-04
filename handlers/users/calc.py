from aiogram import types
import aiogram
from aiogram.dispatcher import FSMContext

from handlers.users.btn import btns
from keyboards.default.btn import btn_main, cancel
from loader import dp
from sheet import *
from states.state import Currency
# Echo bot
@dp.message_handler(text='🧮 Kalkulyator')
async def bot_echo(message: types.Message, state:FSMContext):
    buttons = ['UZS', '💲USD', '🏠 Asosiy menyu']
    data = btns(buttons)
    await message.answer(f"Tanlang!, {message.from_user.full_name}!", reply_markup=data)
    await Currency.name.set()

@dp.message_handler(state=Currency.name, text=['/start', '❌ Bekor qilish'])
async def bot_echo(message: types.Message, state:FSMContext):
    await state.finish()
    await message.answer(text='Tanlang!', reply_markup=btn_main())

@dp.message_handler(state=Currency.name, text=['🏠 Asosiy menyu'])
async def bot_echo(message: types.Message, state:FSMContext):
    await state.finish()
    await message.answer(text='Tanlang!', reply_markup=btn_main())

@dp.message_handler(state=Currency.name)
async def bot_echo(message: types.Message, state:FSMContext):
    name = message.text
    if name == 'UZS':
        name = 'C'
        cur = 2
    else:
        name = 'B'
        cur = 1
    await state.update_data({'name':name})
    await state.update_data({'cur':cur})
    await message.answer(f"Summani kiriting!", reply_markup=cancel())
    await Currency.value.set()

@dp.message_handler(state=Currency.value, text=['/start', '🏠 Asosiy menyu'])
async def bot_echo(message: types.Message, state:FSMContext):
    await state.finish()
    await message.answer(text='Tanlang!', reply_markup=btn_main())

@dp.message_handler(state=Currency.value, text=['⬅️ Orqaga'])
async def bot_echo(message: types.Message, state:FSMContext):
    await Currency.name.set()
    buttons = ['UZS', '💲USD']
    data = btns(buttons)
    await message.answer(text='Tanlang!', reply_markup=data)


@dp.message_handler(state=Currency.value)
async def bot_echo(message: types.Message, state:FSMContext):
    if message.text.isdigit():
        data = await state.get_data()
        name = data.get('name')
        cur = data.get('cur')
        valuta = 'so`m'
        if cur == 2:
            valyuta = "so`m"
        else:
            valyuta = '$'
        value = message.text
        print(name)
        data = await main(value, name, cur)
        print(data)
        # Assuming data[6] contains '2,5' as a percentage string
        percentage_str = data[6].replace(',', '.').replace('%', '')
        percentage_float = float(percentage_str)  # Convert to float
        result = int(percentage_float * float(value) / 100)
        formatted_result = f'{result:,.0f}'
        # limit
        if data[8] == '':
            data[8] = 0
        else:
            data[8] = data[8].replace('%', '')
        limit = int((float(data[5].replace('%', '').replace(",", '.')) + float(data[8]) + float(
            data[6].replace('%', '').replace(",", '.'))) * float(value) + float(value))
        formatted_limit = f'{limit:,.0f}'
        # result
        all = int(result + float(value))
        msg = f"""
<b>Oylik to'lovlar:</b>
6 oyga — ️<b>{data[12]} so`m/oy.</b>
12 oyga — ️<b>{data[18]} so`m/oy.</b>

<b>️Umumiy narxi:</b>
6 oyga — <b>{data[13]} so`m</b>
12 oyga — <b>️{data[19]} so`m</b>

<b>O`rtadagi farq:</b>
6 oyga — <b>{data[14]} so`m</b>
12 oyga — <b>️{data[20]} so`m</b>

• Mahsulotni harid qilish uchun kerakli limit: <b>️{data[9].split(',')[0]} so`m</b>
        """
        await message.answer(text=msg)
        await message.answer(text="Summani kiriting!", reply_markup=cancel())
        await Currency.value.set()
    else:
        await message.answer(text='Faqat son kiriting!')
        await Currency.value.set()
