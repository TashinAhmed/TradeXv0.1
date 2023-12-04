
import numpy as np
from datetime import datetime as dt

def parseDate(date):
    date = date.split("T")[0]
    d = dt.strptime(date, '%Y-%m-%d')
    return d.toordinal()

# Return ordinal date list from candles list
def getOrdinalDate(candles):
    return list(map(lambda x : parseDate(x['time']), candles))

def getDate(candles):
    return list(map(lambda x : x['time'], candles))

# Calculate OHLC value from data object
def calOHLC(obj):
    o = float(obj['o'])
    h = float(obj['h'])
    l = float(obj['l'])
    c = float(obj['c'])
    value = [o, h, l, c]
    return np.mean(value)

# Return OHLC list from candles list
def getOHLC(candles):
    return list(map(lambda x : calOHLC(x['mid']), candles))
    
