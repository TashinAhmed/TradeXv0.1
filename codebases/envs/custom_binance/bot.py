"""
| Author - Tashin Ahmed
| Project - Trading Bot Demo
| Date - 
| Organization - AriSaf Tech Japan K.K.
"""


import config
import json
import websocket
import pprint
import talib
import numpy as np
from binance.client import Client
from binance.enums import *

SOCKET = "wss://testnet.binance.vision/ws/ethusdt@kline_1m"
RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
TRADE_SYMBOL = 'ETHUSD'
TRADE_QUANTITY = 0.05

closes = [] # track series of close values
in_position = False
client = Client(config.API_KEY, config.API_SECRET, tld='us')



def order(side, quantity, symbol, order_type=ORDER_TYPE_MARKET):
    try:
        order = client.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
        print(f"-> Sending Order: {order}")
    except Exception as e:
        return False
    return True

def on_open(ws):
    print("-> Opened Connection")

def on_close(ws):
    print("-> Closed Connection")

def on_message(ws, message):
    global closes # use global closes to track series of close values
    print("-> Received Message: ")
    # print(message)
    json_message = json.loads(message)
    # pprint.pprint(json_message) # pretty printing json files in terminal

    candle = json_message['k']
    is_candle_closed = candle['x']
    close = candle['c']

    if is_candle_closed:
        print(f"Candle closed at {close}.")
        closes.append(float(close)) # it will return a str so converting it to float for further task completion.
        print(f"-- Closes: {closes}")

        if len(closes) > RSI_PERIOD:
            np_closes = np.array(closes)
            rsi = talib.RSI(np_closes, RSI_PERIOD)
            print(f"-- RSI Values so far: {rsi}")
            last_rsi = rsi[-1]
            print(f"-> Current RSI: {last_rsi}")

            if last_rsi > RSI_OVERBOUGHT:
                if in_position:
                    print("SELL NOW")
                    order_succeeded = order(SIDE_SELL, TRADE_QUANTITY, TRADE_SYMBOL)
                    if order_succeeded:
                        in_position = False
                else:
                    print("Already Overbought")

            if last_rsi < RSI_OVERSOLD:
                if in_position:
                    print("Already Oversold")
                else:
                    print("BUY NOW")
                    order_succeeded = order(SIDE_BUY, TRADE_QUANTITY, TRADE_SYMBOL)
                    if order_succeeded:
                        in_position = True

    """
    docs - https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md
    OUTPUT OF PPRINT ABOVE - 

    {'E': 1650828360609,
     'e': 'kline',
     'k': {'B': '0',
           'L': 530300,
           'Q': '0.00000000',
           'T': 1650828359999,
           'V': '0.00000000',
           'c': '2839.33000000',
           'f': 530299,
           'h': '2915.16000000',
           'i': '1m',
           'l': '2839.33000000',
           'n': 2,
           'o': '2915.16000000',
           'q': '808.91617250',
           's': 'ETHUSDT',
           't': 1650828300000,
           'v': '0.27789000',
           'x': True},
     's': 'ETHUSDT'}

    e.g.: 
    
    't' - timestamps; here, 1650828300000 = Mon Apr 25 2022 01:25:00 GMT+0600 (Bangladesh Standard Time)
    reference: https://www.unixtimestamp.com/
    'x' = true means end of the candlestick; false means candlestick is still open and growing.
    """


ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()