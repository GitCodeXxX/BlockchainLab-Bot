from aiogram import Bot, Dispatcher, types, executor
from config import BOT_TOKEN
from ton_api import get_wallet_balance
from xp_system import add_xp, get_xp

bot = Bot(token=7534137870:AAHckWCsRJEG9zquCbu_VSxhz5czRwlmBek)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await message.answer("Willkommen bei BlockchainLab! Sende /balance <wallet> oder /xp.")

@dp.message_handler(commands=['balance'])
async def balance_cmd(message: types.Message):
    args = message.get_args()
    if not args:
        await message.answer("Bitte gib eine Wallet-Adresse an: /balance <wallet>")
        return
    balance = get_wallet_balance(args)
    if balance is not None:
        xp = add_xp(message.from_user.id, 10)
        await message.answer(f"Wallet: {args}\nBalance: {balance:.2f} TON\n+10 XP! (Insgesamt: {xp} XP)")
    else:
        await message.answer("Fehler beim Abrufen der Wallet-Daten.")

@dp.message_handler(commands=['xp'])
async def xp_cmd(message: types.Message):
    xp = get_xp(message.from_user.id)
    await message.answer(f"Dein XP-Stand: {xp} XP")

if __name__ == '__main__':
    executor.start_polling(dp)
