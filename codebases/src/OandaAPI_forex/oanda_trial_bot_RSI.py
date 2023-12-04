#Install Py Package from: https://github.com/hootnot/oanda-api-v20
#https://oanda-api-v20.readthedocs.io/en/latest/oanda-api-v20.html

import json
import oandapyV20 as opy
import oandapyV20.endpoints.instruments as instruments
from oandapyV20.contrib.factories import InstrumentsCandlesFactory

import pandas as pd
from pandas.io.json import json_normalize

from oandapyV20.exceptions import V20Error, StreamTerminated
from oandapyV20.endpoints.transactions import TransactionsStream
from oandapyV20.endpoints.pricing import PricingStream
from oandapyV20.contrib.requests import TrailingStopLossOrderRequest

import datetime
from dateutil import parser

import numpy as np


def exampleAuth():
    accountID, token = None, None
    with open("./oanda_account/account.txt") as I:
        accountID = I.read().strip()
    with open("./oanda_account/token.txt") as I:
        token = I.read().strip()
    return accountID, token


instrument = "EUR_USD"

#Set time functions to offset chart
today = datetime.datetime.today()
two_years_ago = today - datetime.timedelta(days=720)

current_time = datetime.datetime.now()

twentyfour_hours_ago = current_time - datetime.timedelta(hours=12)
print (current_time)
print (twentyfour_hours_ago)

#Create time parameter for Oanada call
ct = current_time.strftime("%Y-%m-%dT%H:%M:%SZ")
tf = twentyfour_hours_ago.strftime("%Y-%m-%dT%H:%M:%SZ")

#Connect to tokens
accountID, access_token = exampleAuth()
client = opy.API(access_token=access_token)

params={"from": tf,
        "to": ct,
        "granularity":'M1',
        "price":'A'}
r = instruments.InstrumentsCandles(instrument=instrument,params=params)
#Do not use client from above
data = client.request(r)
results= [{"time":x['time'],"closeAsk":float(x['ask']['c'])} for x in data['candles']]
df = pd.DataFrame(results).set_index('time')

df.index = pd.DatetimeIndex(df.index)

from oandapyV20.endpoints.pricing import PricingStream
import oandapyV20.endpoints.orders as orders
from oandapyV20.contrib.requests import MarketOrderRequest, TrailingStopLossDetails, TakeProfitDetails
from oandapyV20.exceptions import V20Error, StreamTerminated
import oandapyV20.endpoints.trades as trades

class MomentumTrader(PricingStream):
    def __init__(self, momentum, *args, **kwargs):
        PricingStream.__init__(self, *args, **kwargs)
        self.ticks = 0
        self.position = 0
        self.df = pd.DataFrame()
        self.momentum = momentum
        self.units = 1000
        self.connected = False
        self.client = opy.API(access_token=access_token)

    def create_order(self, units):
        #You can write a custom distance value here, so distance = some calculation

        trailingStopLossOnFill = TrailingStopLossDetails(distance=0.0005)

        order = orders.OrderCreate(accountID=accountID,
                                   data=MarketOrderRequest(instrument=instrument,
                                                           units=units,
                                                           trailingStopLossOnFill=trailingStopLossOnFill.data).data)
        response = self.client.request(order)
        print('\t', response)

    def on_success(self, data):
        self.ticks += 1
        print("ticks=",self.ticks)
        # print(self.ticks, end=', ')

        # appends the new tick data to the DataFrame object
        self.df = self.df.append(pd.DataFrame([{'time': data['time'],'closeoutAsk':data['closeoutAsk']}],
                                 index=[data["time"]]))

        #transforms the time information to a DatetimeIndex object
        self.df.index = pd.DatetimeIndex(self.df["time"])

        # Convert items back to numeric (Why, OANDA, why are you returning strings?)
        self.df['closeoutAsk'] = pd.to_numeric(self.df["closeoutAsk"],errors='ignore')

        # resamples the data set to a new, homogeneous interval, set this from '5s' to '1m'
        dfr = self.df.resample('60s').last().bfill()

        # calculates the log returns
        dfr['returns'] = np.log(dfr['closeoutAsk'] / dfr['closeoutAsk'].shift(1))

        # derives the positioning according to the momentum strategy
        dfr['position'] = np.sign(dfr['returns'].rolling(self.momentum).mean())

        print("position=",dfr['position'].iloc[-1])

        if dfr['position'].iloc[-1] == 1:
            print("go long")
            if self.position == 0:
                self.create_order(self.units)

            elif self.position == -1:
                self.create_order(self.units * 2)
            self.position = 1

        elif dfr['position'].iloc[-1] == -1:
            print("go short")
            if self.position == 0:
                self.create_order(-self.units)


            elif self.position == 1:
                self.create_order(-self.units * 2)

            self.position = -1

        if self.ticks == 25000:
            print("close out the position")
            if self.position == 1:
                self.create_order(-self.units)
            elif self.position == -1:
                self.create_order(self.units)
            self.disconnect()

    def disconnect(self):
        self.connected=False

    def rates(self, account_id, instruments, **params):
        self.connected = True
        params = params or {}
        ignore_heartbeat = None
        if "ignore_heartbeat" in params:
            ignore_heartbeat = params['ignore_heartbeat']
        while self.connected:
            response = self.client.request(self)
            for tick in response:
                if not self.connected:
                    break
                if not (ignore_heartbeat and tick["type"]=="HEARTBEAT"):
                    print(tick)
                    self.on_success(tick)


# Set momentum to be the number of previous 5 second intervals to calculate against

mt = MomentumTrader(momentum=60,accountID=accountID,params={'instruments': instrument})
print(mt)
mt.rates(account_id=accountID, instruments=instrument, ignore_heartbeat=True)

import json
import pandas as pd
from oandapyV20 import API
from oandapyV20.exceptions import V20Error
from oandapyV20.endpoints.pricing import PricingStream

from pandas.io.json import json_normalize

def exampleAuth():
    accountID, token = None, None
    with open("./oanda_account/account.txt") as I:
        accountID = I.read().strip()
    with open("./oanda_account/token.txt") as I:
        token = I.read().strip()
    return accountID, token

#Connect to tokens
accountID, access_token = exampleAuth()
api = API(access_token=access_token, environment="practice")

#instruments = "DE30_EUR,EUR_USD,EUR_JPY"
instruments = "EUR_USD"
s = PricingStream(accountID=accountID, params={"instruments":instruments})

df = pd.DataFrame()
out = pd.DataFrame()

for R in api.request(s):
    df = json_normalize(R)
    out = out.append(df)

out.to_csv('tickdata.csv')


from oandapyV20.endpoints.pricing import PricingStream
import oandapyV20.endpoints.orders as orders
from oandapyV20.contrib.requests import MarketOrderRequest, TrailingStopLossDetails, TakeProfitDetails
from oandapyV20.exceptions import V20Error, StreamTerminated
import oandapyV20.endpoints.trades as trades

class ScalpTrader(PricingStream):
    def __init__(self, momentum, *args, **kwargs):
        PricingStream.__init__(self, *args, **kwargs)
        self.ticks = 0
        self.position = 0
        self.df = pd.DataFrame()
        self.momentum = momentum
        self.units = 1000
        self.connected = False
        self.client = opy.API(access_token=access_token)

    def create_order(self, units):
        #You can write a custom distance value here, so distance = some calculation

        trailingStopLossOnFill = TrailingStopLossDetails(distance=0.0005)

        order = orders.OrderCreate(accountID=accountID,
                                   data=MarketOrderRequest(instrument=instrument,
                                                           units=units,
                                                           trailingStopLossOnFill=trailingStopLossOnFill.data).data)
        response = self.client.request(order)
        print('\t', response)

    def on_success(self, data):
        self.ticks += 1
        print("ticks=",self.ticks)
        # print(self.ticks, end=', ')

        # appends the new tick data to the DataFrame object
        self.df = self.df.append(pd.DataFrame([{'time': data['time'],'closeoutAsk':data['closeoutAsk']}],
                                 index=[data["time"]]))

        #transforms the time information to a DatetimeIndex object
        self.df.index = pd.DatetimeIndex(self.df["time"])

        # Convert items back to numeric (Why, OANDA, why are you returning strings?)
        self.df['closeoutAsk'] = pd.to_numeric(self.df["closeoutAsk"],errors='ignore')

        # resamples the data set to a new, homogeneous interval, set this from '5s' to '1m'
        dfr = self.df.resample('60s').last().bfill()

        #Calculate K and D
        dfr['14-high'] = dfr['closeoutAsk'].rolling(14).max()
        dfr['14-low'] = dfr['closeoutAsk'].rolling(14).min()
        dfr['K'] = (dfr['closeoutAsk'] - dfr['14-low'])*100/(dfr['14-high'] - dfr['14-low'])
        dfr['D'] = dfr['K'].rolling(3).mean()

        # creates position column, fill all with zeros
        dfr['position'] = 0

        # derives the positioning according to the scalping strategy below
        dfr['position'] = np.where(((dfr['D'] > 0) & (dfr['D'] < 20)), 1, dfr.position)
        dfr['position'] = np.where(((dfr['D'] > 80) & (dfr['D'] < 100)), -1, dfr.position)
        print (dfr)

        print("position=",dfr['position'].iloc[-1])
        print ("%K=", dfr['K'].iloc[-1])
        print ("%D=", dfr['D'].iloc[-1])

        if dfr['position'].iloc[-1] == 1:
            print("go long")
            if self.position == 0:
                self.create_order(self.units)

            elif self.position == -1:
                self.create_order(self.units * 2)
            self.position = 1

        elif dfr['position'].iloc[-1] == -1:
            print("go short")
            if self.position == 0:
                self.create_order(-self.units)


            elif self.position == 1:
                self.create_order(-self.units * 2)

            self.position = -1

        if self.ticks == 25000:
            print("close out the position")
            if self.position == 1:
                self.create_order(-self.units)
            elif self.position == -1:
                self.create_order(self.units)
            self.disconnect()

    def disconnect(self):
        self.connected=False

    def rates(self, account_id, instruments, **params):
        self.connected = True
        params = params or {}
        ignore_heartbeat = None
        if "ignore_heartbeat" in params:
            ignore_heartbeat = params['ignore_heartbeat']
        while self.connected:
            response = self.client.request(self)
            for tick in response:
                if not self.connected:
                    break
                if not (ignore_heartbeat and tick["type"]=="HEARTBEAT"):
                    print(tick)
                    self.on_success(tick)


from oandapyV20.endpoints.pricing import PricingStream
import oandapyV20.endpoints.orders as orders
from oandapyV20.contrib.requests import MarketOrderRequest, TrailingStopLossDetails, TakeProfitDetails
from oandapyV20.exceptions import V20Error, StreamTerminated
import oandapyV20.endpoints.trades as trades

class ScalpTraderRSI(PricingStream):
    def __init__(self, momentum, *args, **kwargs):
        PricingStream.__init__(self, *args, **kwargs)
        self.ticks = 0
        self.position = 0
        self.df = pd.DataFrame()
        self.momentum = momentum
        self.units = 10000
        self.connected = False
        self.client = opy.API(access_token=access_token)

    def create_order(self, units):
        #You can write a custom distance value here, so distance = some calculation

        trailingStopLossOnFill = TrailingStopLossDetails(distance=0.05)

        order = orders.OrderCreate(accountID=accountID,
                                   data=MarketOrderRequest(instrument=instrument,
                                                           units=units,
                                                           trailingStopLossOnFill=trailingStopLossOnFill.data).data)
        response = self.client.request(order)
        print('\t', response)

    def on_success(self, data):
        self.ticks += 1
        print("ticks=",self.ticks)
        # print(self.ticks, end=', ')

        # appends the new tick data to the DataFrame object
        self.df = self.df.append(pd.DataFrame([{'time': data['time'],'closeoutAsk':data['closeoutAsk']}],
                                 index=[data["time"]]))

        #transforms the time information to a DatetimeIndex object
        self.df.index = pd.DatetimeIndex(self.df["time"])

        # Convert items back to numeric (Why, OANDA, why are you returning strings?)
        self.df['closeoutAsk'] = pd.to_numeric(self.df["closeoutAsk"],errors='ignore')

        # resamples the data set to a new, homogeneous interval, set this from '5s' to '1m'
        dfr = self.df.resample('300s').last().bfill()

        #Calculate K and D
        delta = dfr['closeoutAsk'].diff()
        up = delta.clip(lower=0)
        down = -1*delta.clip(upper=0)
        ema_up = up.ewm(com=0.5, min_periods=13).mean()
        ema_down = down.ewm(com=0.5, min_periods=13).mean()
        rs = ema_up/ema_down

        dfr['RSI'] = 100 - (100/(1 + rs))

        # creates position column, fill all with zeros
        dfr['position'] = 0

        # derives the positioning according to the scalping strategy below
        dfr['position'] = np.where(((dfr['RSI'] > 0) & (dfr['RSI'] < 10)), 1, dfr.position)
        dfr['position'] = np.where(((dfr['RSI'] > 80) & (dfr['RSI'] < 100)), -1, dfr.position)
        print (dfr)

        print("position=",dfr['position'].iloc[-1])
        print ("RSI=", dfr['RSI'].iloc[-1])


        if dfr['position'].iloc[-1] == 1:
            print("go long")
            if self.position == 0:
                self.create_order(self.units)

            elif self.position == -1:
                self.create_order(self.units * 2)
            self.position = 1

        elif dfr['position'].iloc[-1] == -1:
            print("go short")
            if self.position == 0:
                self.create_order(-self.units)


            elif self.position == 1:
                self.create_order(-self.units * 2)

            self.position = -1

        if self.ticks == 25000:
            print("close out the position")
            if self.position == 1:
                self.create_order(-self.units)
            elif self.position == -1:
                self.create_order(self.units)
            self.disconnect()

    def disconnect(self):
        self.connected=False

    def rates(self, account_id, instruments, **params):
        self.connected = True
        params = params or {}
        ignore_heartbeat = None
        if "ignore_heartbeat" in params:
            ignore_heartbeat = params['ignore_heartbeat']
        while self.connected:
            response = self.client.request(self)
            for tick in response:
                if not self.connected:
                    break
                if not (ignore_heartbeat and tick["type"]=="HEARTBEAT"):
                    print(tick)
                    self.on_success(tick)