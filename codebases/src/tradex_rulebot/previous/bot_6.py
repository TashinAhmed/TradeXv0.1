from alpaca_trade_api.rest import REST, TimeFrame
import pandas as pd
import datetime
import logging
import math

BASE_URL = "https://paper-api.alpaca.markets"

KEY_ID= ""
SECRET_KEY = ""


currenttime = datetime.datetime.now()
hours = currenttime.strftime('%H')
minutes = currenttime.strftime('%M')
seconds = currenttime.strftime('%S')
today = currenttime.day
month = currenttime.month
year = currenttime.year

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
bars = api.get_crypto_bars("ETHUSD", TimeFrame.Minute).df

# Filter data by exchange
bars = bars[bars.exchange == 'CBSE']




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


# Returns a series with the MACD
def get_macd(price, slow=SMA_SLOW, fast=SMA_FAST, smooth=9):
    price = price.to_frame()
    exp1 = price.ewm(span = fast, adjust = False).mean()
    exp2 = price.ewm(span = slow, adjust = False).mean()
    macd = pd.DataFrame(exp1 - exp2).rename(columns = {'close':'macd'})
    signal = pd.DataFrame(macd.ewm(span = smooth, adjust = False).mean()).rename(columns = {'macd':'signal'})
    hist = pd.DataFrame(macd['macd'] - signal['signal']).rename(columns = {0:'hist'})
    frames =  [macd, signal, hist]
    srs = pd.concat(frames, join = 'inner', axis = 1)
    # print(srs)
    print(srs.macd)
    return macd.squeeze()

# Returns a series with the BB Up and Down
def get_bollinger_bands(prices, rate=20):
    sma = get_sma(prices, rate)
    std = prices.rolling(rate).std()
    bollinger_up = sma + std * 2 # Calculate top band
    bollinger_down = sma - std * 2 # Calculate bottom band
    return bollinger_up, bollinger_down

# Returns the Force Index 
def ForceIndex(data, ndays): 
    FI = pd.Series(data['Close'].diff(ndays) * data['Volume'], name = 'ForceIndex') 
    data = data.join(FI) 
    return data



def avg_true_range(self, df): 
  ind = range(0,len(df))
  indexlist = list(ind)
  df.index = indexlist

  for index, row in df.iterrows():
    if index != 0:
      tr1 = row["High"] - row["Low"]
      tr2 = abs(row["High"] - df.iloc[index-1]["Close"])
      tr3 = abs(row["Low"] - df.iloc[index-1]["Close"])

      true_range = max(tr1, tr2, tr3)
      df.set_value(index,"True Range", true_range)

  df["Avg TR"] = df["True Range"].rolling(min_periods=14, window=14, center=False).mean()
  return df


def chandelier_exit(self, df): # default period is 22
  df_tr = self.avg_true_range(df)
  rolling_high = df_tr["High"][-22:].max()
  rolling_low = df_tr["Low"][-22:].max()
  chandelier_long = rolling_high - df_tr.iloc[-1]["Avg TR"] * 3
  chandelier_short = rolling_low - df_tr.iloc[-1]["Avg TR"] * 3
  return chandelier_long, chandelier_short


# Checks whether we should buy (fast ma > slow ma)
def get_signal(fast, slow):
    return fast[-1] > slow[-1], fast[-1], slow[-1]

# Get up-to-date 1 minute data from Alpaca and add the moving averages
def get_bars(symbol):
    bars = api.get_crypto_bars(symbol, TimeFrame.Minute).df
    bars = bars[bars.exchange == 'CBSE']
    
    # print("TYPE BARS", type(bars))              # dataframe
    # print("TYPE BARS CLOSE", type(bars.close))  # series

    bars[f'sma_fast'] = get_sma(bars.close, SMA_FAST)
    bars[f'sma_slow'] = get_sma(bars.close, SMA_SLOW)
    bars[f'bb_up'], bars[f'bb_down'] = get_bollinger_bands(bars.close)
    bars[f'macd_bar'] = get_macd(bars.close)



    # print("BARS BARS BARS")
    # print(bars)
    return bars

# initialization of current_time_order; w/o init it will throw error.
current_time_order = datetime.now()
print("CURRENT TIME ORDER ", type(current_time_order))
PROFITS = 0

while True:
    # GET DATA
    bars = get_bars(symbol=SYMBOL)
    
    # CHECK POSITIONS
    position = get_position(symbol=SYMBOL)
    should_buy, fast_signal, slow_signal = get_signal(bars.sma_fast,bars.sma_slow)
    print(f"position: {position}")

    # changes made if we have balance more than closing price. 
    if should_buy == True and INIT_BALANCE + PROFITS > bars.close[-1]:
        try:
            api.submit_order(SYMBOL, qty=QTY_PER_TRADE, side='buy',  type='market', time_in_force='gtc')
            print(f'Fast {fast_signal} / Slow: {slow_signal} / Position: {position} / Should Buy: {should_buy} / Symbol: {SYMBOL} / close price: {bars.close[-1]} / Side: BUY / Quantity: {QTY_PER_TRADE}')
            PROFITS = PROFITS - (bars.close[-1] * QTY_PER_TRADE) 
            logging.info('Symbol: {: >7} | Position: {: >4} | close price: {: >8} | Side: {: >4} 🟢 | Profits: {: >9.2f} | Quantity: {: >4} 🤑'.format(SYMBOL, math.ceil(position), bars.close[-1], "BUY", PROFITS, QTY_PER_TRADE))
            
            current_close_price = bars.close[-1]
            MAX_CLOSE_PRICE = max(current_close_price, MAX_CLOSE_PRICE)
            
        except:
            logging.warning('{} Insufficient buying power'.format(datetime.datetime.now().strftime("%x %X")))
            print('Trading in process '+ datetime.datetime.now().strftime("%x %X") + ' Insufficient fund')
            pass
    
    elif position >= 0.1 and should_buy == False:
        try:
            api.submit_order(SYMBOL, qty=QTY_PER_TRADE, side='sell', type='market', time_in_force='gtc')
            PROFITS = PROFITS + (bars.close[-1] * QTY_PER_TRADE)
            print(f'Fast {fast_signal} / Slow: {slow_signal} / Position: {position} / Should Buy: {should_buy} / Symbol: {SYMBOL} / close price: {bars.close[-1]} / Side: SELL / Quantity: {QTY_PER_TRADE}')
            logging.info('Symbol: {: >7} | Position: {: >4} | close price: {: >8} | Side: {: >4} 🔴 | Profits: {: >9.2f} | Quantity: {: >4} 💵'.format(SYMBOL, math.ceil(position), bars.close[-1], "SELL", PROFITS, QTY_PER_TRADE))
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
            print(f'Fast {fast_signal} / Slow: {slow_signal} / Position: {position} / Should Buy: {should_buy} / Symbol: {SYMBOL} / close price: {bars.close[-1]} / Side: SELL / Quantity: {int(position)+1}')
            logging.info('Symbol: {: >7} | Position: {: >4} | close price: {: >8} | Side: {: >4} 🔴 | Profits: {: >9.2f} | Quantity: {: >4} 💵'.format(SYMBOL, math.ceil(position), bars.close[-1], "SELL", PROFITS, int(position)+1))
        except Exception as e:
            # print('No sell', signal, e)
            pass

    comp_print = datetime.now() - current_time_order
    
    print("COMP_PRINT: ", comp_print)
    print("SELL TIME: ", sell_time)
    print("CLOSE PRICE: ", bars.close[-1])
    
    time.sleep(get_pause())
    