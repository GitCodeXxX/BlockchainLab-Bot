@dp.message_handler(commands=['app'])
async def open_webapp(message: types.Message):
    kb = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(
        text="Öffne BlockchainLab MiniApp",
        web_app=types.WebAppInfo(url="https://deinname.github.io/deinrepo/webapp/")
    )
    kb.add(btn)
    await message.answer("Hier ist deine MiniApp:", reply_markup=kb)