from aiogram import types

from handlers.users.btn import menejer
from keyboards.default.btn import btn_main
from loader import dp
from sheet import find_user


@dp.message_handler(text='💰Balans')
async def bot_start(message: types.Message):
    data = await find_user(value_to_find=message.from_user.id)
    if data == None:
        text = """
⚠️ Siz hali rasmiy ro’yhatdan o’tmagansiz! Iltimos, hamkorlar bo’limiga bog’laning va biz bilan hamkorlik asosida, savdolaringizni oshiring!

📞 Aloqa uchun: (33) 090-78-49
        """

        await message.answer(text=text, reply_markup=menejer())
    else:
        print(data)
        text = f"""
ℹ️ Do'kon ma'lumotlari:
— do'kon nomi: {data[6]}
— guvohnoma raqami: {data[7]}

🤑 Umumiy hisob:
— yangi buyurtma: {data[14]}
— konsultatsiya: {data[15]}
— rasmiylashtirilmoqda: {data[16]}
— rasmiylashtirildi: {data[17]}
— yetkazilmoqda: {data[18]}
— sotilmadi: {data[20]}
— bekor qilindi: {data[21]}
— limit ajratilmadi: {data[22]}
— limit yetmadi: {data[23]}
— sotildi: {data[19]}

✅ Umumiy yechib olindi: {data[24]}
💲 Joriy balans: {data[25]}

😉 Zo’r ketyapsiz! Biz bilan faqat rivojlanishni istaganlar birga, shuning uchun hamkorligimizga ko’z tegmasin.
"""

        await message.answer(text=text)


