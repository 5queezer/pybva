import secrets
import socketio
import requests
from binance.client import Client

sio = socketio.Client(engineio_logger=False)

@sio.event
def connect():
    print("I'm connected!")

@sio.event
def disconnect():
    print("I'm disconnected!")

@sio.event
def message(data):
    print("message: ", data)

@sio.event
def buy_signal(data):
    print("buy_signal: ", data)

@sio.event
def sell_signal(data):
    print("sell_signal: ", data)

@sio.event
def close_traded_signal(data):
    print("close_traded_signal: ", data)

@sio.event
def stop_traded_signal(data):
    print("stop_traded_signal: ", data)

@sio.event
def user_payload(data):
    print("user_payload: ", data)

def updateopentrades():
    url = "https://bitcoinvsaltcoins.com/api/useropentradedsignals?key=" + secrets.bva_api_key
    response = requests.get(url)
    response.raise_for_status()
    print("updateopentrades: ", response.json())

    updateopentrades()


url = 'https://nbt-hub.herokuapp.com/?type=client&key=' + secrets.bva_api_key
sio.connect(url)
sio.wait()

# client = Client(secrets.binance_api_key, secrets.binance_api_secret)
