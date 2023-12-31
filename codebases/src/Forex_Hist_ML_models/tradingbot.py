#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Sun May 20 13:39:06 2018
@author: Tashin
"""
import numpy as np
import datetime
import warnings
import pprint
import json
import time
from connection import Connection
from helpers import candlesparser
from models import svr
from modules import orders
from modules import positions
from modules import priceinfo
from modules import historicaldata
from modules import accountsummary
from sklearn.exceptions import DataConversionWarning

# for 1d array deprecation warning
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=DataConversionWarning)

# Load config
connection = Connection()
config = connection.config
instruments = config['INSTRUMENTS'].split(',')
day_range = config['DAY_RANGE'].split(',')
selected_range = config['SELECTED_RANGE']
granularity = config['GRANULARITY']
kernel = config['SVR_KERNEL']
limit_unit = int(config['LIMIT_UNIT'])
order_unit = int(config['ORDER_UNIT'])
min_profit = float(config['MIN_PROFIT'])
limit_margin = int(config['LIMIT_MARGIN'])
cut_loss_limit = float(config['CUT_LOSS_LIMIT'])

# Get current price
now = datetime.datetime.now()
print('************ {} ************\n'.format(str(now)))
price_info = priceinfo.getCurrentPrice(config['INSTRUMENTS'])
currencies = priceinfo.parsePriceInfo(price_info)

# Account summary
print('************ Account ************\n')
summary = accountsummary.getSummary()
account = summary['account']
available_margin = float(account['marginAvailable'])
print('Account Summary:')
pprint.pprint(summary)

# Run regression once per day
print('\n************ Regression ************\n')
regressors = {}
today = time.strftime("%Y-%m-%d", time.localtime())
with open('svrdate.txt', 'r') as f:
    last_record_date = f.read()
with open('record.json', 'r') as f:
    last_record = json.load(f)

if today == last_record_date and last_record:
    # Get regression data when regression already run today
    regressors = last_record
    print('Already run regression in {}.\n'.format(today))
else:
    # Loop different day range
    # Get last N days candles
    for instrument in instruments:
        for day in day_range:
            data = historicaldata.getData(instrument, day, granularity)
            candles = data['candles']
            date_list = candlesparser.getDate(candles)
            x = candlesparser.getOrdinalDate(candles)
            x = np.vstack(x)
            y = candlesparser.getOHLC(candles)
            y = np.vstack(y)
            
            # Build random svr model and store it in dict
            result = svr.buildModel(x, y, instrument, kernel)
            if instrument in regressors.keys():
                regressors[instrument][day] = result
            else:
                regressors[instrument] = {}
                regressors[instrument][day] = result

    # Record the regression data
    with open('record.json', 'w') as f:
        f.write(json.dumps(regressors, indent = 2))
    with open('svrdate.txt', 'w') as f:
        f.write(today)

# Get Account open position
position_res = positions.getOpenPosition()
print('************ Positions ************\n')
print('Account Open Position:')
pprint.pprint(position_res)
print('\n************ Results ************\n')


# Strategy
for instrument in instruments:
    # Regressor predict
    predict_wk = regressors[instrument][selected_range]['predict_wk']
    day_mean = regressors[instrument][selected_range]['day_mean']
    
    # Current Info
    tradeable = currencies[instrument]['tradeable']
    ask = currencies[instrument]['ask']
    bid = currencies[instrument]['bid']
    
    # Account current position
    # Instrument can be None when no previous position with current instrument
    instrument_list = list(filter(lambda pos : pos['instrument'] == instrument, position_res['positions']))
    instrument_pos = instrument_list[0] if len(instrument_list) > 0 else None
    long = instrument_pos['long'] if instrument_pos is not None else None
    average_price = float(long['averagePrice']) if long is not None else None
    units = int(long['units']) if long is not None else 0
        
    # Flag
    is_rising = predict_wk > ask
    above_mean = day_mean < ask
    is_cheaper = average_price > ask if average_price is not None else above_mean
    below_limit = limit_unit >= order_unit + units
    make_profit = bid > average_price + min_profit if average_price is not None else False
    cut_loss = bid < average_price - cut_loss_limit if average_price is not None else False
    no_margin = available_margin < limit_margin
    
    # Logic
    if tradeable:
        # Create Order
        if make_profit:
            # 'Sell' Logic
            # - sell all units when profit higher than min config
            diff = bid - average_price
            profit = diff * units
            order_res = orders.createOrder(str(-units), instrument)
            print('Trading bot sold all {}, around {} units, earn for {}'.format(instrument, units, profit))
        elif cut_loss:
            # Cut Loss Logic
            # - sell all units when bid price lower than cut loss percentage
            diff = average_price - bid
            loss = diff * units
            order_res = orders.createOrder(str(-units), instrument)
            print('Trading bot sold all {}, around {} units, loss for {}'.format(instrument, units, loss))
        elif no_margin:
            # no enough margin
            print('Account dont have enough available margin for trading.')
        elif is_rising and is_cheaper and below_limit:
            # 'Buy' Logic
            # - Future trend, currency rising
            # - AND Cheaper than previous order 
            # - OR exceed N day average at first purchase
            # - Wont order too much on single currency

            # Create Order
            order_res = orders.createOrder(str(order_unit), instrument)
            print('Trading bot created order on {}, bought {} units.\n'.format(instrument, order_unit))
            # print('Order Creation: {}\n'.format(order_res))
        else:
            print('Trading bot wont take action on {} at this moment.\n'.format(instrument))
    else:
        print('{} currently not available, so cannot create order.\n'.format(instrument))
    


    
