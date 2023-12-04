import numpy as np
import pandas as pd
from ta.trend import EMAIndicator
from ta.volatility import BollingerBands

from config import *
from indicators import *
from proc_indicators_intersection import *
from stage_one import *

import matplotlib.pyplot as plt
# plt.style.use('fivethirtyeight')

if __name__ == "__main__":
    
    # read files
    df = pd.read_csv(DATA_PATH)
    df = add_indicators(df)

    # handle NaN values
    df.fillna(0, inplace = True)
    
    len_df = len(df) # return type int 974 w/o title row (another row with col header still exists)
    # print(len_df)

    # calculation of indicators intersection between EMA 20,100,200 and BBH,BBL
    indicatorsIntersection(df)
    # print(df)

    # stage one - buy and sell
    emaInterestionTrend(df, len_df, current_balance, trace, trace2, counter, pips, keeper_balance, HIGHEST_TRACE_LIMIT)
    # print("counter: ", counter) # called from inside emaInterestionTrend()

    # vizualization
    fig, ax = plt.subplots(figsize=(14,8))
    ax.plot(df['Close'], linewidth=0.5, color='blue', alpha = 0.9, label='_nolegend_')
    ax.plot(df['ema100'], label = 'EMA 01', alpha = 0.85)
    ax.plot(df['ema200'], label = 'EMA 02' , alpha = 0.85)
    # ax.plot(df['BBH'], label = 'BBH', alpha = 0.85)
    # ax.plot(df['BBL'], label = 'BBL', alpha = 0.85)
    ax.scatter(df.index , df['Buy'] , label = 'Buy' , marker = '^', color = 'green',alpha =1 )
    ax.scatter(df.index , df['Sell'] , label = 'Sell' , marker = 'v', color = 'red',alpha =1 )
    ax.set_title(" Price History with buy and sell signals",fontsize=10, backgroundcolor='blue', color='white')
    ax.set_xlabel(f'timestamp' ,fontsize=18)
    ax.set_ylabel('Close Price JPY (₨)' , fontsize=18)
    legend = ax.legend()
    ax.grid()
    plt.tight_layout()
    plt.show()



    # print(df)