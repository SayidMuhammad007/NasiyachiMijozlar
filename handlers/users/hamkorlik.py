from aiogram import types

from keyboards.default.btn import btn_main
from loader import dp


@dp.message_handler(text='🤝 Hamkorlik')
async def bot_start(message: types.Message):
    msg = """Do'koningizdagi savdolarni oshirishga nima deysiz?

— Bizni muddatli to'lov tizimimiz bilan buni imkoni bor!

🤔 Nega biz bilan ishlashingiz kerak?
1. Sotuvlaringizni O'zbekiston bo'ylab oshirishga imkon beramiz!
2. Brendingizni ko'proq tanitishga yordam beramiz!
3. Qog'ozbozlikdan ozod qilamiz!
4. Nasiya-savdoni tizimli yuritishga yordam beramiz!
5. Sizni doimo eshitamiz va takliflaringizni realizatsiya qilamiz!

———————————————

❓ Nasiyachi.savdogar - muddatli to’lov tizimi qanday ishlaydi?

1. Mijoz do’koningizdan muddatli to’lovga mahsulotni tanlaydi!
2. Mijozning plastik kartasining aylanmasiga garab, mijoz chun 100 million so'mgacha ya'ni mablag' ajratib beramiz!
3. Mijoz limitdan foydalangan holda mahsulotingizni harid giladi!
4. Loyihamiz, mahsulot uchun to'lovni 3 kun, kamdan kam hollarda 5 kunda o'tkazib beradi!
5. Mijoz jadvalga muvofiq bizga oylik to'lovni amalga oshirib boraveradi!

😉 Biz bilan bog'laning va bugundan muddatli to'lovga mahsulot sotishni boshlang!

📞 (33) 090-78-49
    """

    await message.answer(text=msg, reply_markup=btn_main())

