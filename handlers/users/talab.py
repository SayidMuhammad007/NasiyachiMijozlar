from aiogram import types

from keyboards.default.btn import btn_main
from loader import dp


@dp.message_handler(text='📃 Nasiya savdoning talab va shartlari')
async def bot_start(message: types.Message):
    msg = """✅ Nasiyachi.biz do'konidan muddatli to'lovga mahsulot harid qilish talab va shartlari!

• Sizga kerak bo'ladi:
— Pasport yoki ID karta (original)
— Plastik karta (HUMO&UZCARD)

• Shartlar esa quyidagicha:
— 22 yoshdan 65 yoshgacha bo'lish;
— pasport yoki ID karta ma'lumotlarini taqdim etish;
— O‘zbekiston Respublikasi fuqarosi bo‘lish;
— oxirgi 3 oy davomida 1 million so‘mdan ortiq oylik tushumga ega, oxirgi 4 oy ichida faol bo'lgan asosiy daromadga ega Uzcard yoki Humo kartasiga ega bo'lish;
— pasport yoki ID karta  va plastik karta bitta insonga tegishli bo'lishi lozim;

😊 Yuqoridagi talab va shartlarga to'g'ri kelsangiz, Siz uchun albatta muddatli to'lovni rasmiylashtirib beramiz!

😉 Biz bilan bog'laning va bugunoq o'z mahsulotingizdan foydalanishni boshlang!

📞 (94) 342-88-99
"""

    await message.answer(text=msg, reply_markup=btn_main())

