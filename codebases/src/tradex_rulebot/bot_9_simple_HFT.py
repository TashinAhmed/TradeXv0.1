from alpaca_trade_api import REST, TimeFrame
import pandas as pd
import random
import time
from datetime import datetime, timedelta
import math 

BASE_URL = "https://paper-api.alpaca.markets"

KEY_ID= ""
SECRET_KEY = ""  

SYMBOL = "BTCUSD"
SMA_FAST = 12
SMA_SLOW = 24
QTY_PER_TRADE = 1


# instantiate REST API
api = REST(key_id=KEY_ID, secret_key=SECRET_KEY, base_url=BASE_URL)

# get 1 min bar 
bars = api.get_crypto_bars("BTCUSD", TimeFrame.Minute).df
bars = bars[bars.exchange == 'CBSE']

def get_pause():
    now = datetime.now()
    next_min = now.replace(second=0, microsecond=0) + timedelta(minutes=1)
    pause = math.ceil((next_min - now).seconds)
    print(f"Sleep for {pause}")
    return pause

def get_position(symbol):
    positions = api.list_positions()
    for position in positions:
        if position.symbol == symbol:
            return float(position.qty)
    return 0

def get_sma(series, periods):
    return series.rolling(periods).mean()

def get_signal_sma(fast, slow):
    print(f"Fast {fast[-1]}  /  Slow: {slow[-1]}")
    return fast[-1] > slow[-1]

def get_bars_sma(symbol):
    bars = api.get_crypto_bars(symbol, TimeFrame.Minute).df
    bars = bars[bars.exchange == 'CBSE']
    bars[f'sma_fast'] = get_sma(bars.close, SMA_FAST)
    bars[f'sma_slow'] = get_sma(bars.close, SMA_SLOW)
    return bars


while True:
    bars_sma = get_bars_sma(symbol=SYMBOL)
    position = get_position(symbol=SYMBOL)
    should_buy_sma = get_signal_sma(bars_sma.sma_fast,bars_sma.sma_slow)
    print(f"Position: {position} / Should Buy: {should_buy_sma}")
    
    if should_buy_sma == True:
        api.submit_order(SYMBOL, qty=QTY_PER_TRADE, side='buy', type='market', time_in_force='gtc')
        print(f'Symbol: {SYMBOL} / Side: BUY / Quantity: {QTY_PER_TRADE}')
    
    elif position > 0 and should_buy_sma == False:
        api.submit_order(SYMBOL, qty=QTY_PER_TRADE, side='sell', type='market', time_in_force='gtc')
        print(f'Symbol: {SYMBOL} / Side: SELL / Quantity: {QTY_PER_TRADE}')

    time.sleep(get_pause())
    print("-"*20)