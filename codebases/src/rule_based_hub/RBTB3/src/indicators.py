import numpy as np
import pandas as pd
from ta.trend import EMAIndicator
from ta.volatility import BollingerBands

def add_indicators(df):
    # storing all indicators value prior to calculating the next one
    df["ema20"] = EMAIndicator(close=df["Close"], window=20, fillna=True).ema_indicator()
    df["ema100"] = EMAIndicator(close=df["Close"], window=30, fillna=True).ema_indicator()
    df["ema200"] = EMAIndicator(close=df["Close"], window=50, fillna=True).ema_indicator()
    
    indicator_bb = BollingerBands(close=df["Close"], window=20, window_dev=2)
    df['BBH'] = indicator_bb.bollinger_hband()
    df['BBL'] = indicator_bb.bollinger_lband()
    
    return df