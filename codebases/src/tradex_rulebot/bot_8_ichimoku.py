from alpaca_trade_api.rest import REST, TimeFrame
import pandas as pd
import datetime
import logging
import math

BASE_URL = "https://paper-api.alpaca.markets"

KEY_ID = ''
SECRET_KEY = ''


currenttime = datetime.datetime.now()
hours = currenttime.strftime('%H')
minutes = currenttime.strftime('%M')
seconds = currenttime.strftime('%S')
today = currenttime.day
month = currenttime.month
year = currenttime.year

# ichimoku cloud variables
tenkan_window = 9 # 20
kijun_window = 26 # 60
senkou_span_b_window = 26 # 120
cloud_displacement = 30
chikou_shift = -26 # -30


# WARNING: direct assignment set the sell_time in datetime.timedelta format. 
sell_time = datetime.datetime(year, month, today, 0,5,0) - datetime.datetime(year, month, today, 0,0,0)

log_path = "logs/"
log_filename = f"bot_6_{today}_{month}_{hours}_{minutes}.log"

logging.basicConfig(
    filename= log_path + log_filename,
    level=logging.INFO,
    format='%(levelname)s %(asctime)s %(message)s')

# Instantiate REST API Connection
api = REST(key_id=KEY_ID,secret_key=SECRET_KEY,base_url="https://paper-api.alpaca.markets")

# Fetch 1Minute historical bars of Bitcoin
bars_historical = api.get_crypto_bars('ETHUSD', TimeFrame.Minute, "2022-10-18", "2022-10-19").df
bars_historical = bars_historical[bars_historical.exchange == 'CBSE']

bars = api.get_crypto_bars("ETHUSD", TimeFrame.Minute).df
bars = bars[bars.exchange == 'CBSE']

bars = pd.concat([bars_historical, bars], ignore_index=True)
bars[f'chikou_span'] = bars.close.shift(chikou_shift) # chikou span needs pre shifting thus it needs to be initiated early

# print("BARS LEN: ", len(bars.close))

# print("HISTORICAL BARS")
# print(bars_historical.index)


# print("BARS")
# print(bars.index)

# print(len(bars_historical))
# print(len(bars.close))



from datetime import datetime, timedelta
import math
import time

SYMBOL = 'ETHUSD'
SMA_FAST = 12
SMA_SLOW = 24
QTY_PER_TRADE = 1
QTY_PER_SELL = 0
MAX_CLOSE_PRICE = 0.0000000000001
INIT_BALANCE = 100000000
BAR_TIME = 0



################## SMA OBSERVATIONS ##################
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


# Description is given in the article
def get_pause():
    now = datetime.now()
    next_min = now.replace(second=0, microsecond=0) + timedelta(minutes=1)
    pause = math.ceil((next_min - now).seconds)
    # logging.warning(f"Sleep for {pause}")
    print(f"Sleep for {pause} 💤")
    return pause

# Same as the function in the random version
def get_position(symbol):
    positions = api.list_positions()
    for p in positions:
        if p.symbol == symbol:
            return float(p.qty)
    return 0

# Returns a series with the moving average
def get_sma(series, periods):
    return series.rolling(periods).mean()

# Checks whether we should buy (fast ma > slow ma)
# def get_signal(fast, slow):
#     return fast[-1] > slow[-1], fast[-1], slow[-1]

# ichimoku cloud calls 
def get_signal(close, tenkan, kijun, senkou_a, senkou_b, chikou):
    # if api.account.trading_blocked:
    # 	print('Account is currently restricted from trading.')
    # pass
    print("close: {: >4} tenkan_prev: {: >4} tenkan: {: >4} kijun: {: >4} senkou_a: {: >4} senkou_b: {: >4} chikou: {: >4} close_chikou: {: >4}".format(close[-1], tenkan[-2], tenkan[-1], kijun[-1], senkou_a[-1], senkou_b[-1], chikou[-28], close[-28]))
    print(f"CONDITIONS BUY: {kijun[-2] > tenkan[-2]}, {kijun[-1] <= tenkan[-1]}, {close[-1] > senkou_a[-1]}, {close[-1] > senkou_b[-1]}, {chikou[-28] > close[-28]}")
    print(f"CONDITIONS SELL: {kijun[-2] < tenkan[-2]}, {kijun[-1] >= tenkan[-1]}, {close[-1] < senkou_a[-1]}, {close[-1] < senkou_b[-1]}, {chikou[-28] < close[-28]}")

    logging.info("close: {: >4} tenkan_prev: {: >4} tenkan: {: >4} kijun: {: >4} senkou_a: {: >4} senkou_b: {: >4} chikou: {: >4} close_chikou: {: >4}".format(close[-1], tenkan[-2], tenkan[-1], kijun[-1], senkou_a[-1], senkou_b[-1], chikou[-28], close[-28]))
    logging.warning(f"CONDITIONS BUY: {kijun[-2] > tenkan[-2]}, {kijun[-1] <= tenkan[-1]}, {close[-1] > senkou_a[-1]}, {close[-1] > senkou_b[-1]}, {chikou[-28] > close[-28]}")
    logging.warning(f"CONDITIONS SELL: {kijun[-2] < tenkan[-2]}, {kijun[-1] >= tenkan[-1]}, {close[-1] < senkou_a[-1]}, {close[-1] < senkou_b[-1]}, {chikou[-28] < close[-28]}")

    if(kijun[-2] > tenkan[-2] and kijun[-1] <= tenkan[-1] and close[-1] > senkou_a[-1] and close[-1] > senkou_b[-1] and chikou[-28] > close[-28] 
        or chikou[-28] > close[-28] and senkou_a[-1] > senkou_b[-1] and close[-1] <= senkou_a[-1] and close[-1] >= senkou_b[-1]
        or senkou_b[-2] > senkou_a[-2] and senkou_a[-1] >= senkou_b[-1]):
        return "BUY"
    if(kijun[-2] < tenkan[-2] and kijun[-1] >= tenkan[-1] and close[-1] < senkou_a[-1] and close[-1] < senkou_b[-1] and chikou[-28] < close[-28]
        or chikou[-28] < close[-28] and senkou_a[-1] < senkou_b[-1] and close[-1] >= senkou_a[-1] and close[-1] <= senkou_b[-1]
        or senkou_b[-2] < senkou_a[-2] and senkou_a[-1] <= senkou_b[-1]):
        return "SELL"
    # return "HOLD"


# Get up-to-date 1 minute data from Alpaca and add the moving averages
def get_bars(symbol):
    bars = api.get_crypto_bars(symbol, TimeFrame.Minute).df
    bars = bars[bars.exchange == 'CBSE']
    # print("TYPE BARS", type(bars))              # dataframe
    # print("TYPE BARS CLOSE", type(bars.close))  # series
    # bars[f'sma_fast'] = get_sma(bars.close, SMA_FAST)
    # bars[f'sma_slow'] = get_sma(bars.close, SMA_SLOW)
    # print("BARS BARS BARS")
    # print(bars)

    # Tenkan 
    tenkan_sen_high = bars.high.rolling(window=tenkan_window).max()
    tenkan_sen_low = bars.low.rolling(window=tenkan_window).min()
    bars[f'tenkan_sen'] = (tenkan_sen_high + tenkan_sen_low) /2

    # Kijun 
    kijun_sen_high = bars.high.rolling( window=kijun_window ).max()
    kijun_sen_low = bars.low.rolling( window=kijun_window ).min()
    bars[f'kijun_sen'] = (kijun_sen_high + kijun_sen_low) / 2

    # Senkou Span A 
    bars[f'senkou_span_a'] = ((bars['tenkan_sen'] + bars['kijun_sen']) / 2).shift(cloud_displacement)
    
    # Senkou Span B 
    senkou_span_b_high = bars.high.rolling( window=senkou_span_b_window ).max()
    senkou_span_b_low = bars.low.rolling( window=senkou_span_b_window ).min()
    bars[f'senkou_span_b'] = ((senkou_span_b_high + senkou_span_b_low) / 2).shift(cloud_displacement)
    
    # Chikou
    bars[f'chikou_span'] = bars.close.shift(chikou_shift)

    return bars

# initialization of current_time_order; w/o init it will throw error.
current_time_order = datetime.now()
print("CURRENT TIME ORDER ", current_time_order)
PROFITS = 0

while True:
    # GET DATA
    bars = get_bars(symbol=SYMBOL)
    bars_sma = get_bars_sma(symbol=SYMBOL)
    # CHECK POSITIONS
    position = get_position(symbol=SYMBOL)
    # should_buy, fast_signal, slow_signal = get_signal(bars.sma_fast,bars.sma_slow)
    
    # ichimoku cloud signal
    if (len(bars.chikou_span) < 28):
        print(f"re run after {28-len(bars.chikou_span)} minutes")
        logging.warning(f"re run after {28-len(bars.chikou_span)} minutes")
        time.sleep(get_pause())
    else:
        should_buy = get_signal(bars.close, bars.tenkan_sen, bars.kijun_sen, bars.senkou_span_a, bars.senkou_span_b, bars.chikou_span)
        should_buy_sma = get_signal_sma(bars_sma.sma_fast,bars_sma.sma_slow)
        print(f"position: {position}")

        # changes made if we have balance more than closing price. 
        if (should_buy == "BUY" or should_buy_sma == True) and INIT_BALANCE + PROFITS > bars.close[-1]:
            try:
                api.submit_order(SYMBOL, qty=QTY_PER_TRADE, side='buy',  type='market', time_in_force='gtc')
                PROFITS = PROFITS - (bars.close[-1] * QTY_PER_TRADE)
                if should_buy_sma == True:
                    print(f'SMA Triggered - Position: {position} / Should Buy: {should_buy} / Symbol: {SYMBOL} / close price: {bars.close[-1]} / Side: BUY / Quantity: {QTY_PER_TRADE}')
                    logging.info('Symbol: {: >7} | Position: {: >4} | close price: {: >8} | Side: {: >4} 🔴 | Profits: {: >9.2f} | Quantity: {: >4} 🤑'.format(SYMBOL, math.ceil(position), bars.close[-1], "BUY", PROFITS, QTY_PER_TRADE))    
                else:
                    print(f'Position: {position} / Should Buy: {should_buy} / Symbol: {SYMBOL} / close price: {bars.close[-1]} / Side: BUY / Quantity: {QTY_PER_TRADE}')
                    logging.info('Symbol: {: >7} | Position: {: >4} | close price: {: >8} | Side: {: >4} 🔴 | Profits: {: >9.2f} | Quantity: {: >4} 🤑'.format(SYMBOL, math.ceil(position), bars.close[-1], "BUY", PROFITS, QTY_PER_TRADE))
                
                current_close_price = bars.close[-1]
                MAX_CLOSE_PRICE = max(current_close_price, MAX_CLOSE_PRICE)
                
            except:
                logging.warning('{} Insufficient buying power'.format(datetime.datetime.now().strftime("%x %X")))
                print('Trading in process '+ datetime.datetime.now().strftime("%x %X") + ' Insufficient fund')
                pass
        
        elif position >= 0.1 and (should_buy == "SELL" or should_buy_sma == False):
            try:
                api.submit_order(SYMBOL, qty=QTY_PER_TRADE, side='sell', type='market', time_in_force='gtc')
                PROFITS = PROFITS + (bars.close[-1] * QTY_PER_TRADE)
                print(f'Position: {position} / Should Buy: {should_buy} / Symbol: {SYMBOL} / close price: {bars.close[-1]} / Side: SELL / Quantity: {QTY_PER_TRADE}')
                logging.info('Symbol: {: >7} | Position: {: >4} | close price: {: >8} | Side: {: >4} 🟢 | Profits: {: >9.2f} | Quantity: {: >4} 💵'.format(SYMBOL, math.ceil(position), bars.close[-1], "SELL", PROFITS, QTY_PER_TRADE))
                current_time_order = datetime.now()
                print(f"LAST SELL TIME: {current_time_order}, CLOSE PRICE: {current_close_price}, MAX_CLOSE_PRIC_LAST_BUY: {MAX_CLOSE_PRICE}")
            except Exception as e:
                # print('No sell', signal, e)
                pass
        
        # if we are at freezing state for 5 minutes have bought more than 1 trades and current close price is higher than the maximum ordered value: sell everything immediately. 
        elif datetime.now() - current_time_order >= sell_time and position >= 1 and MAX_CLOSE_PRICE < bars.close[-1]:
            try:
                api.submit_order(SYMBOL, qty=int(position)+1, side='sell', type='market', time_in_force='gtc')
                PROFITS = PROFITS + (bars.close[-1] * (int(position)+1) )
                print(f'Position: {position} / Should Buy: {should_buy} / Symbol: {SYMBOL} / close price: {bars.close[-1]} / Side: SELL / Quantity: {int(position)+1}')
                logging.info('Symbol: {: >7} | Position: {: >4} | close price: {: >8} | Side: {: >4} 🟢 | Profits: {: >9.2f} | Quantity: {: >4} 💵'.format(SYMBOL, math.ceil(position), bars.close[-1], "SELL", PROFITS, int(position)+1))
            except Exception as e:
                # print('No sell', signal, e)
                pass

        comp_print = datetime.now() - current_time_order
        
        # print("COMP_PRINT: ", comp_print)
        # print("SELL TIME: ", sell_time)
        # print("CLOSE PRICE: ", bars.close[-1])
        
        time.sleep(get_pause())
    