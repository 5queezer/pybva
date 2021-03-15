import secrets
import asyncio
import socketio
import requests

url_nbt = 'https://nbt-hub.herokuapp.com/?type=client&key=' + secrets.bva_api_key
url_bva = "https://bitcoinvsaltcoins.com/api/useropentradedsignals?key=" + secrets.bva_api_key

sio = socketio.AsyncClient()
stratids = []


@sio.event
async def connect():
    print("I'm connected!")


@sio.event
async def disconnect():
    print("I'm disconnected!")


@sio.event
async def message(data):
    print("message: ", data)


@sio.event
async def buy_signal(data):
    print("buy_signal: ", data)


@sio.event
async def sell_signal(data):
    print("sell_signal: ", data)


@sio.event
async def close_traded_signal(data):
    print("close_traded_signal: ", data)


@sio.event
async def stop_traded_signal(data):
    print("stop_traded_signal: ", data)


@sio.event
def user_payload(data):
    for strategy in data:
        if strategy['trading'] == True and strategy['trading_type'] == 'real':
            stratids.append(strategy['stratid'])


async def update_open_trades():
    response = requests.get(url_bva)
    response.raise_for_status()
    print("updateopentrades: ", response.json())


async def main():
    await update_open_trades()
    await sio.connect(url_nbt)
    await sio.wait()


if __name__ == '__main__':
    asyncio.run(main())
