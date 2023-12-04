import pandas as pd
from ta.trend import SMAIndicator
from ta.volatility import BollingerBands



def add_indicators(df):
    df["sma20"] = SMAIndicator(close=df["Close"], window=20, fillna=True).sma_indicator()
    df["sma100"] = SMAIndicator(close=df["Close"], window=100, fillna=True).sma_indicator()
    df["sma200"] = SMAIndicator(close=df["Close"], window=200, fillna=True).sma_indicator()
    
    indicator_bb = BollingerBands(close=df["Close"], window=20, window_dev=2)
    df['bb_bbh'] = indicator_bb.bollinger_hband()
    df['bb_bbl'] = indicator_bb.bollinger_lband()

    return df



if __name__ == "__main__":
    df = pd.read_csv("./BTC_USD.csv")
    df = df.sort_values('Date')
    df = add_indicators(df)

    len_df = len(df)
    
    ''' STORAGES START '''

    

    sma_100_200_diff = []   # differences of SMA 100 and 200
    bb_diff = []    # differences of Bollinger bands high and low storage

    sma_100_200_diff_buy = []   # 1. If the difference between 100 and 200 SMA is positive, basic instance - buy toggle.
    sma_100_200_diff_sell = []  # 2. If the difference between 100 and 200 SMA is negative, basic instance - sell toggle.
    bb_diff_buy = []    # 1. If the difference between BB is positive, basic instance - buy toggle.
    bb_diff_sell = []   # 2. If the difference between BB is negative, basic instance -  sell toggle.

    sma_100_buy = []    # if df["sma100"][i] is bigger than df["sma100"][i-1] give buy signal (basic instance)
    sma_100_sell = []   # if df["sma100"][i] is smaller than df["sma100"][i-1] give sell signal (basic instance)
    sma_200_buy = []    # if df["sma200"][i] is bigger than df["sma200"][i-1] give buy signal (basic instance)
    sma_200_sell = []   # if df["sma200"][i] is smaller than df["sma200"][i-1] give sell signal (basic instance)

    sma_100_bb_bbh_buy = []     # if sma100 intersect bb_bbh trigger buy
    sma_200_bb_bbh_buy = []     # if sma200 intersect bb_bbh trigger buy
    sma_100_bb_bbl_sell = []    # if sma100 intersect bb_bbl trigger sell
    sma_200_bb_bbl_sell = []    # if sma200 intersect bb_bbl trigger sell

    BUY_SELL_FLAG = []  # if sma100 greater than sma200 or sma200 greater than sma100 then trigger buy and sell
    BUY_SELL_SIGNAL = [] # ultimate buy and sell signal

    # initial appending
    sma_100_buy.append(0)
    sma_100_sell.append(0)
    sma_200_buy.append(0)
    sma_200_sell.append(0)
    sma_100_bb_bbh_buy.append(0)
    sma_200_bb_bbh_buy.append(0)
    sma_100_bb_bbl_sell.append(0)
    sma_200_bb_bbl_sell.append(0)
    BUY_SELL_FLAG.append("-")
    BUY_SELL_SIGNAL.append("-")

    ''' STORAGES END '''
    # ##################################################################################################################################################################################################################
    # ##################################################################################################################################################################################################################
    # ##################################################################################################################################################################################################################
    # ##################################################################################################################################################################################################################



    # storing through iteration 
    for i in range(len_df):
        sma_100_200_diff.append(df["sma100"][i] - df["sma200"][i])
        bb_diff.append(df["bb_bbh"][i] - df["bb_bbl"][i])
    
    

    # saving the diffs in df
    df["sma_100_200_diff"] = sma_100_200_diff
    df["bb_diff"] = bb_diff

    # initially bb values are void; filled that up with zeroes
    df.fillna(0, inplace = True)

    

    for i in range(len_df):
        
        ''' SOLVING BUY AND SELL FOR 100 and 200 SMA'''

        # 1. If the difference between 100 and 200 SMA is positive, then set status buy.
        if(df["sma_100_200_diff"][i] > 0):
            sma_100_200_diff_buy.append(1)
        else:
            sma_100_200_diff_buy.append(0)

        # 2. If the difference between 100 and 200 SMA is negative, then set status sell.
        if(df["sma_100_200_diff"][i] < 0):
            sma_100_200_diff_sell.append(1)
        else:
            sma_100_200_diff_sell.append(0)

        ''' SOLVING BUY AND SELL FOR BB '''        
        
        # 1. If the difference between BB is positive, then set status buy.
        if(df["bb_diff"][i] > 0):
            bb_diff_buy.append(1)
        else:
            bb_diff_buy.append(0)
        # 2. If the difference between BB is negative, then set status sell.
        if(df["bb_diff"][i] < 0):
            bb_diff_sell.append(1)
        else:
            bb_diff_sell.append(0)

    # saving the buy and sell values in df for sma100 and sma200 diff
    df["sma_100_200_diff_buy"] = sma_100_200_diff_buy
    df["sma_100_200_diff_sell"] = sma_100_200_diff_sell
    df["bb_diff_buy"] = bb_diff_buy
    df["bb_diff_sell"] = bb_diff_sell






    
    for i in range(1, len_df):
        # if df["sma100"][i] is bigger than df["sma100"][i-1] give buy signal
        if(df["sma100"][i] > df["sma100"][i-1]):
            sma_100_buy.append(1)
        else:
            sma_100_buy.append(0)

        # if df["sma100"][i] is smaller than df["sma100"][i-1] give sell signal
        if(df["sma100"][i] < df["sma100"][i-1]):
            sma_100_sell.append(1)
        else:
            sma_100_sell.append(0)

        # if df["sma200"][i] is bigger than df["sma200"][i-1] give buy signal
        if(df["sma200"][i] > df["sma200"][i-1]):
            sma_200_buy.append(1)
        else:
            sma_200_buy.append(0)

        # if df["sma200"][i] is smaller than df["sma200"][i-1] give sell signal
        if(df["sma200"][i] < df["sma200"][i-1]):
            sma_200_sell.append(1)
        else:
            sma_200_sell.append(0)

        # if sma100 intersect bb_bbh trigger buy
        if(df["sma100"][i-1] > df["bb_bbh"][i-1] and df["sma100"][i] > df["bb_bbh"][i]) or (df["sma100"][i-1] < df["bb_bbh"][i-1] and df["sma100"][i] < df["bb_bbh"][i]):
            sma_100_bb_bbh_buy.append(1)
        else:
            sma_100_bb_bbh_buy.append(0)

        # if sma200 intersect bb_bbh trigger buy
        if(df["sma200"][i-1] > df["bb_bbh"][i-1] and df["sma200"][i] > df["bb_bbh"][i]) or (df["sma200"][i-1] < df["bb_bbh"][i-1] and df["sma200"][i] < df["bb_bbh"][i]):
            sma_200_bb_bbh_buy.append(1)
        else:
            sma_200_bb_bbh_buy.append(0)

        # if sma100 intersect bb_bbl trigger sell
        if(df["sma100"][i-1] > df["bb_bbl"][i-1] and df["sma100"][i] > df["bb_bbl"][i]) or (df["sma100"][i-1] < df["bb_bbl"][i-1] and df["sma100"][i] < df["bb_bbl"][i]):
            sma_100_bb_bbl_sell.append(1)
        else:
            sma_100_bb_bbl_sell.append(0)

        # if sma200 intersect bb_bbl trigger sell
        if(df["sma200"][i-1] > df["bb_bbl"][i-1] and df["sma200"][i] > df["bb_bbl"][i]) or (df["sma200"][i-1] < df["bb_bbl"][i-1] and df["sma200"][i] < df["bb_bbl"][i]):
            sma_200_bb_bbl_sell.append(1)
        else:
            sma_200_bb_bbl_sell.append(0)
    
    # saving the buy and sell values in df
    df["sma_100_buy"] = sma_100_buy
    df["sma_100_sell"] = sma_100_sell
    df["sma_200_buy"] = sma_200_buy
    df["sma_200_sell"] = sma_200_sell
    
    df["sma_100_bb_bbh_buy"] = sma_100_bb_bbh_buy
    df["sma_200_bb_bbh_buy"] = sma_200_bb_bbh_buy
    df["sma_100_bb_bbl_sell"] = sma_100_bb_bbl_sell
    df["sma_200_bb_bbl_sell"] = sma_200_bb_bbl_sell

    # ##################################################################################################################################################################################################################
    # ##################################################################################################################################################################################################################
    # ##################################################################################################################################################################################################################
    # ##################################################################################################################################################################################################################
    
    

    # if sma100 greater than sma200 or sma200 greater than sma100 then trigger UP and DOWN

    for i in range(1, len_df):
        if(df["sma100"][i-1] > df["sma200"][i-1] and df["sma100"][i] > df["sma200"][i]):
            BUY_SELL_FLAG.append("UP")
            if(
            # sma_100_200_diff_sell[i]==1 and 
            # bb_diff_sell[i]==1 and 
            # sma_100_sell[i]==1 and 
            sma_200_sell[i]==1 and 
            # sma_100_bb_bbl_sell[i]==1 and 
            sma_200_bb_bbl_sell[i]==1):
                BUY_SELL_SIGNAL.append("SELL")
            else:
                BUY_SELL_SIGNAL.append("-")
        elif(df["sma100"][i-1] < df["sma200"][i-1] and df["sma100"][i] < df["sma200"][i]):
            if(
            # sma_100_200_diff_buy[i]==1 and 
            # bb_diff_buy[i]==1 and 
            # sma_100_buy[i]==1 and 
            sma_200_buy[i]==1 and 
            # sma_100_bb_bbh_buy[i]==1 and 
            sma_200_bb_bbh_buy[i]==1):
                BUY_SELL_SIGNAL.append("BUY")
            else:
                BUY_SELL_SIGNAL.append("-")
            BUY_SELL_FLAG.append("DOWN")
        else:
            BUY_SELL_FLAG.append("_")
            BUY_SELL_SIGNAL.append("-")

    df["BUY_SELL_FLAG"] = BUY_SELL_FLAG
    df["BUY_SELL_SIGNAL"] = BUY_SELL_SIGNAL

    print(df["BUY_SELL_SIGNAL"].unique())

    df.to_csv('outcome.csv')
    # print(df)