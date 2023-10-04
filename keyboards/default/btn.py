from handlers.users.btn import btns

def btn_main():
    buttons = ['🧮 Kalkulyator', '🤝 Hamkorlik', '📃 Nasiya savdoning talab va shartlari']
    data = btns(buttons)
    return data

def cancel():
    buttons = ['🏠 Asosiy menyu','⬅️ Orqaga']
    data = btns(buttons)
    return data
