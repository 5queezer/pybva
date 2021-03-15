import secrets
from binance.client import Client

client = Client(secrets.binance_api_key, secrets.binance_api_secret)
system = client.get_system_status()

if system['status'] != 0:
    raise BaseException(system['message'])


def get_btc_price():
    return float(client.get_avg_price(symbol='BTCUSDT')['price'])


# balance = client.futures_account_balance()
# account_info = client.futures_account()
# print(balance)
# print(account_info)
print(get_btc_price())
