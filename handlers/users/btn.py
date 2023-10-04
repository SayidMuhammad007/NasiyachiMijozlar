from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def btns(request):
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for i in request:
        btn.insert(i)
    return btn

def Cancel():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn.add('Bekor qilish')
    return btn

def menejer():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="👤 Menejer", callback_data="manager", url="http://t.me/ikromoffuzb")]
    ])
    return keyboard