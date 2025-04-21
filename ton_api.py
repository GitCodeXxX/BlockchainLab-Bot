import requests
from config import TON_API_KEY, TON_API_URL

def get_wallet_balance(address):
    params = {
        "address": address,
        "key": TON_API_KEY
    }
    response = requests.get(f"{TON_API_URL}/getAddressBalance", params=params)
    if response.status_code == 200:
        balance = int(response.json()["result"]) / 1e9
        return balance
    return None
