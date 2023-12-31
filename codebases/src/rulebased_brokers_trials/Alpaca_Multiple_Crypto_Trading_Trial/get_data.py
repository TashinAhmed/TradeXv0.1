#------ IMPORT LIBRARY and CONFIG -------#
from alpaca_trade_api.rest import REST, TimeFrame
from config import *
import pandas as pd


pd.options.display.max_rows = 999
pd.set_option('display.max_columns', None)

from pytz import timezone


tz = timezone('EST')

def get_sma(series, periods):
    return series.rolling(periods).mean()

class StockInfo(object):
    def __init__(self, symbols, rate, slow, fast, loading):
        self.symbols = symbols
        self.rate = rate
        self.slow = slow
        self.fast = fast
        self.loading = loading

    def get_minute_bar(self):
        try:
            # Add Position Info #
            ticker = [x.symbol for x in api.list_positions()]
            qty = [x.qty for x in api.list_positions()]
            avg_entry_price = [x.avg_entry_price for x in api.list_positions()]

            my_position = dict(zip(ticker, qty))
            entry_price = dict(zip(ticker, avg_entry_price))
            # data = api.get_barset(self.symbols, self.rate, limit=20).df
            data = api.get_crypto_bars(self.symbols, self.rate, limit=10).df
            data = data[data.exchange == 'CBSE']     

            # CONSTRUCT STOCK DATAFRAME INFO HERE
            for x in self.symbols:
                data[f'sma_fast'] = get_sma(data.close, self.fast)
                data[f'sma_slow'] = get_sma(data.close, self.slow)


                # data.loc[:, (x, 'fast_ema_1min')] = data[x]['close'].rolling(window=self.fast).mean()
                # data.loc[:, (x, 'slow_ema_20min')] = data[x]['close'].rolling(window=self.slow).mean()
                # data.loc[:, (x, 'return_1_min')] = (data[x]['close'] - data[x]['close'].shift(1)) / (data[x]['close'].shift(1))
                data.loc[:, (x, 'loading')] = int(loading[x])
                
                if x in ticker:
                    data.loc[:, (x, 'qty')] = int(my_position[x])
                    # print("my position ", my_position)
                    # data.loc[:, (x, 'qty')] = (my_position[x])
                    data.loc[:, (x, 'entry_price')] = float(entry_price[x])
                else:
                    data.loc[:, (x, 'qty')] = 0
                    data.loc[:, (x, 'entry_price')] = 0

                print("DATA DATA DATA")
                print(data)
            return data
            
        except ConnectionError as e:
            print("There might be connection errors")
            pass

    def get_signals(self):
        data = self.get_minute_bar()
        signals = {}

        # CONSTRUCT SIGNALS HERE
        for x in self.symbols:

            if (data[x].iloc[-1]['sma_fast'] >= data[x].iloc[-1]['sma_slow']):
                signal = (data[x].iloc[-1]['loading'])

            # Sell-out signal - number of shares to be liquidated is the value of signal
            else:
                signal = (data[x].iloc[-1]['qty'])*(-1)
            signals[x] = signal

        return signals

if __name__ == '__main__':

    # ------ GET STOCK DATAFRAME -----#
    stock_data = StockInfo(symbols, freq, slow, fast, loading)

    #------ GET TRADING SIGNALS -----#
    signals = stock_data.get_signals()
    print("SIGNALS: ", signals)


