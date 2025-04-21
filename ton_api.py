import requests
from config import TON_API_KEY, TON_API_URL

def get_wallet_balance(address):
    params = {
        "address": address,
        "key": 96a333a8ff4b2c9f9d4d7d70419dc566f6a2a2497faa6be6cb40d78e1d716197
    }
    response = requests.get(f"{TON_API_URL}/getAddressBalance", params=params)
    if response.status_code == 200:
        balance = int(response.json()["result"]) / 1e9
        return balance
    return None
