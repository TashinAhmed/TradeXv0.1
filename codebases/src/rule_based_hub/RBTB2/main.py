import numpy as np
import pandas as pd
from ta.trend import EMAIndicator
from ta.volatility import BollingerBands

def add_indicators(df):
    # storing all indicators value prior to calculating the next one
    df["ema20"] = EMAIndicator(close=df["Close"], window=20, fillna=True).ema_indicator()
    df["ema100"] = EMAIndicator(close=df["Close"], window=100, fillna=True).ema_indicator()
    df["ema200"] = EMAIndicator(close=df["Close"], window=200, fillna=True).ema_indicator()
    
    indicator_bb = BollingerBands(close=df["Close"], window=20, window_dev=2)
    df['bb_bbh'] = indicator_bb.bollinger_hband()
    df['bb_bbl'] = indicator_bb.bollinger_lband()

    return df


if __name__ == "__main__":
    df = pd.read_csv("./jpy_usd.csv")
    df = df.sort_values('Date')
    df = add_indicators(df)

    df.fillna(0, inplace = True)
    
    len_df = len(df) # return type int 5036 with header row
    
    # print("dataframe length: ",len_df)
    # print('\n\nDATAFRAME\n',df)


    threshold_closeprice_with_indicators = float(input("Enter threshold difference for close price - indicators: "))
    threshold_ema_slope_calc_01 = int(input("Enter threshold for EMA slope calc 01: "))
    threshold_ema_slope_calc_02 = int(input("Enter threshold for EMA slope calc 02: "))
    threshold_ema_slope_calc_03 = int(input("Enter threshold for EMA slope calc 03: "))
    threshold_closevalue = float(input("Enter threshold for close value: "))
    threshold_closevalue_ema_01 = float(input("Enter threshold for close value EMA distance calc 01: "))
    threshold_closevalue_ema_02 = float(input("Enter threshold for close value EMA distance calc 02: "))
    threshold_closevalue_ema_03 = float(input("Enter threshold for close value EMA distance calc 03: "))

    ema_20_100_diff = []    # differences of EMA 20 and 200
    ema_100_200_diff = []   # differences of EMA 100 and 200   
    ema_20_200_diff = []    # differences of EMA 100 and 200
    ema100_BBH_diff = []    # differences of EMA 100 and BBH
    ema200_BBH_diff = []    # differences of EMA 200 and BBH
    ema100_BBL_diff = []    # differences of EMA 100 and BBL
    ema200_BBL_diff = []    # differences of EMA 200 and BBL
    #----------------------------------------------------------------------------------------------------------------------------------------------------------
    '''
    # bb_diff = []    # differences of Bollinger bands high and low storage

    # ema_100_200_diff_buy = []   # 1. If the difference between 100 and 200 SMA is positive, basic instance - buy toggle.
    # ema_100_200_diff_sell = []  # 2. If the difference between 100 and 200 SMA is negative, basic instance - sell toggle.
    # bb_diff_buy = []    # 1. If the difference between BB is positive, basic instance - buy toggle.
    # bb_diff_sell = []   # 2. If the difference between BB is negative, basic instance -  sell toggle.

    # ema_100_buy = []    # if df["sma100"][i] is bigger than df["sma100"][i-1] give buy signal (basic instance)
    # ema_100_sell = []   # if df["sma100"][i] is smaller than df["sma100"][i-1] give sell signal (basic instance)
    # ema_200_buy = []    # if df["sma200"][i] is bigger than df["sma200"][i-1] give buy signal (basic instance)
    # ema_200_sell = []   # if df["sma200"][i] is smaller than df["sma200"][i-1] give sell signal (basic instance)

    # ema_100_bb_bbh_buy = []     # if sma100 intersect bb_bbh trigger buy
    # ema_200_bb_bbh_buy = []     # if sma200 intersect bb_bbh trigger buy
    # ema_100_bb_bbl_sell = []    # if sma100 intersect bb_bbl trigger sell
    # ema_200_bb_bbl_sell = []    # if sma200 intersect bb_bbl trigger sell

    # BUY_SELL_FLAG = []  # if sma100 greater than sma200 or sma200 greater than sma100 then trigger buy and sell
    # BUY_SELL_SIGNAL = [] # ultimate buy and sell signal

    # initial appending
    # ema_100_buy.append(0)
    # ema_100_sell.append(0)
    # ema_200_buy.append(0)
    # ema_200_sell.append(0)
    # ema_100_bb_bbh_buy.append(0)
    # ema_200_bb_bbh_buy.append(0)
    # ema_100_bb_bbl_sell.append(0)
    # ema_200_bb_bbl_sell.append(0)
    # BUY_SELL_FLAG.append("-")
    # BUY_SELL_SIGNAL.append("-") '''


    # storing differences between every indicators
    # currently stored indicators -
    #     EMA 20
    #     EMA 100
    #     EMA 200
    #     bollinger band high
    #     bollinger band low
    # if difference changes to positive to negative or vice versa it will tell whether they intersected or not.

    ema_20_100_diff = df["ema20"] - df["ema100"]
    ema_100_200_diff = df["ema100"] - df["ema200"]
    ema_20_200_diff = df["ema20"] - df["ema200"]
    ema100_BBH_diff = df["ema100"] - df["bb_bbh"]
    ema200_BBH_diff = df["ema200"] - df["bb_bbh"]
    ema100_BBL_diff = df["ema100"] - df["bb_bbl"]
    ema200_BBL_diff = df["ema200"] - df["bb_bbl"]
    
    df["ema_20_100_diff"] = ema_20_100_diff
    df["ema_100_200_diff"] = ema_100_200_diff
    df["ema_20_200_diff"] = ema_20_200_diff
    df["ema100_BBH_diff"] = ema100_BBH_diff
    df["ema200_BBH_diff"] = ema200_BBH_diff
    df["ema100_BBL_diff"] = ema100_BBL_diff
    df["ema200_BBL_diff"] = ema200_BBL_diff


    # flags(they will throw bianry outcome) whether the indicator lines intersects or not
    ema_20_100_flag = []
    ema_100_200_flag = []
    ema_20_200_flag = []
    ema100_BBH_flag = []
    ema200_BBH_flag = []
    ema100_BBL_flag = []
    ema200_BBL_flag = []

    # init appending (as we won't count init timestamp)
    ema_20_100_flag.append(0)
    ema_100_200_flag.append(0)
    ema_20_200_flag.append(0)
    ema100_BBH_flag.append(0)
    ema200_BBH_flag.append(0)
    ema100_BBL_flag.append(0)
    ema200_BBL_flag.append(0)

    # (1A) and (1B) trigger values for buy and sell
    ema_20_100_trigger = 0
    ema_100_200_trigger = 0
    ema_20_200_trigger = 0
    ema100_BBH_trigger = 0
    ema200_BBH_trigger = 0
    ema100_BBL_trigger = 0
    ema200_BBL_trigger = 0

    # (3) close price vs indicators
    flag_close_100ema = []
    flag_close_200ema = []
    flag_close_BBU = []
    flag_close_BBL = []

    trigger_close_100ema = 0
    trigger_close_200ema = 0
    trigger_close_BBU = 0
    trigger_close_BBL = 0

    flag_close_100ema.append(0)
    flag_close_200ema.append(0)
    flag_close_BBU.append(0)
    flag_close_BBL.append(0)
        

    temp_count = 0
    TRIGGER = 0

    minm_close_ema100 = 0
    minm_close_ema200 = 0
    minm_close_bb_bbh = 0
    minm_close_bb_bbl = 0


    for i in range(1,len_df):

        if(df["ema_20_100_diff"][i] > 0):
            ema_20_100_flag.append(1)
        elif(df["ema_20_100_diff"][i] < 0):
            ema_20_100_flag.append(0)
        elif(df["ema_20_100_diff"][i] == 0 and i > 0):
            ema_20_100_flag.append(ema_20_100_flag[i-1])
        
        # ema_20_100_trigger = 1 if (ema_20_100_flag[i] != ema_20_100_flag[i-1] and i > 0) else 0

        if(ema_20_100_flag[i] != ema_20_100_flag[i-1] and i > 0):
            ema_20_100_trigger = 1
        else:
            ema_20_100_trigger = 0



        if(df["ema_100_200_diff"][i] > 0):
            ema_100_200_flag.append(1)
        elif(df["ema_100_200_diff"][i] < 0):
            ema_100_200_flag.append(0)
        elif(df["ema_100_200_diff"][i] == 0 and i > 0):
            ema_100_200_flag.append(ema_100_200_flag[i-1])

        if(ema_100_200_flag[i] != ema_100_200_flag[i-1] and i > 0):
            ema_100_200_trigger = 1
        else:
            ema_100_200_trigger = 0

        if(df["ema_20_200_diff"][i] > 0):
            ema_20_200_flag.append(1)
        elif(df["ema_20_200_diff"][i] < 0):
            ema_20_200_flag.append(0)
        elif(df["ema_20_200_diff"][i] == 0 and i > 0):
            ema_20_200_flag.append(ema_20_200_flag[i-1])
        
        if(ema_20_200_flag[i] != ema_20_200_flag[i-1] and i > 0):
            ema_20_200_trigger = 1
        else:
            ema_20_200_trigger = 0

        if(df["ema100_BBH_diff"][i] > 0):
            ema100_BBH_flag.append(1)
        elif(df["ema100_BBH_diff"][i] < 0):
            ema100_BBH_flag.append(0)
        elif(df["ema100_BBH_diff"][i] == 0 and i > 0):
            ema100_BBH_flag.append(ema100_BBH_flag[i-1])
        
        if(ema100_BBH_flag[i] != ema100_BBH_flag[i-1] and i > 0):
            ema100_BBH_trigger = 1
        else:
            ema100_BBH_trigger = 0

        if(df["ema200_BBH_diff"][i] > 0):
            ema200_BBH_flag.append(1)
        elif(df["ema200_BBH_diff"][i] < 0):
            ema200_BBH_flag.append(0)
        elif(df["ema200_BBH_diff"][i] == 0 and i > 0):
            ema200_BBH_flag.append(ema200_BBH_flag[i-1])

        if(ema200_BBH_flag[i] != ema200_BBH_flag[i-1] and i > 0):
            ema200_BBH_trigger = 1
        else:
            ema200_BBH_trigger = 0
        
        if(df["ema100_BBL_diff"][i] > 0):
            ema100_BBL_flag.append(1)
        elif(df["ema100_BBL_diff"][i] < 0):
            ema100_BBL_flag.append(0)
        elif(df["ema100_BBL_diff"][i] == 0 and i > 0):
            ema100_BBL_flag.append(ema100_BBL_flag[i-1])

        if(ema100_BBL_flag[i] != ema100_BBL_flag[i-1] and i > 0):
            ema100_BBL_trigger = 1
        else:
            ema100_BBL_trigger = 0

        if(df["ema200_BBL_diff"][i] > 0):
            ema200_BBL_flag.append(1)
        elif(df["ema200_BBL_diff"][i] < 0):
            ema200_BBL_flag.append(0)
        elif(df["ema200_BBL_diff"][i] == 0 and i > 0):
            ema200_BBL_flag.append(ema200_BBL_flag[i-1])
        
        if(ema200_BBL_flag[i] != ema200_BBL_flag[i-1] and i > 0):
            ema200_BBL_trigger = 1
        else:
            ema200_BBL_trigger = 0


        # (3) close price vs indicators
        if(i==1):
            minm_close_ema100 = abs(df["Close"][i-1] - df["ema100"][i-1])
            minm_close_ema200 = abs(df["Close"][i-1] - df["ema200"][i-1])
            minm_close_bb_bbh = abs(df["Close"][i-1] - df["bb_bbh"][i-1])
            minm_close_bb_bbl = abs(df["Close"][i-1] - df["bb_bbl"][i-1])
        else:
            minm_close_ema100 = min(abs(df["Close"][i] - df["ema100"][i]), minm_close_ema100)
            minm_close_ema200 = min(abs(df["Close"][i] - df["ema200"][i]), minm_close_ema200)
            minm_close_bb_bbh = min(abs(df["Close"][i] - df["bb_bbh"][i]), minm_close_bb_bbh)
            minm_close_bb_bbl = min(abs(df["Close"][i] - df["bb_bbl"][i]), minm_close_bb_bbl)

        if(abs(df["Close"][i] - df["ema100"][i]) <= threshold_closeprice_with_indicators):
            flag_close_100ema.append(1)
        else:
            flag_close_100ema.append(0)

        if(flag_close_100ema[i] != flag_close_100ema[i-1] and i > 0):
            trigger_close_100ema = 1
        else:
            trigger_close_100ema = 0
        

        if(abs(df["Close"][i] - df["ema200"][i]) <= threshold_closeprice_with_indicators):
            flag_close_200ema.append(1)
        else:
            flag_close_200ema.append(0)
        
        if(flag_close_200ema[i] != flag_close_200ema[i-1] and i > 0):
            trigger_close_200ema = 1
        else:
            trigger_close_200ema = 0


        if(abs(df["Close"][i] - df["bb_bbh"][i]) <= threshold_closeprice_with_indicators):
            flag_close_BBU.append(1)
        else:
            flag_close_BBU.append(0)

        if(flag_close_BBU[i] != flag_close_BBU[i-1] and i > 0):
            trigger_close_BBU = 1
        else:
            trigger_close_BBU = 0
        
        if(abs(df["Close"][i] - df["bb_bbl"][i]) <= threshold_closeprice_with_indicators):
            flag_close_BBL.append(1)
        else:
            flag_close_BBL.append(0)

        if(flag_close_BBL[i] != flag_close_BBL[i-1] and i > 0):
            trigger_close_BBL = 1
        else:
            trigger_close_BBL = 0

        # 1A or 1B or 3  
        if(ema_20_100_trigger==1 
            and ema_100_200_trigger==1 
            and ema_20_200_trigger==1
            or ema100_BBH_trigger==1 
            and ema200_BBH_trigger==1 
            and ema100_BBL_trigger==1 
            and ema200_BBL_trigger==1
            or trigger_close_100ema==1
            and trigger_close_200ema==1
            and trigger_close_BBU==1
            and trigger_close_BBL==1
            ):
            temp_count += 1
            # print("Buy Signal at: ", i)
            TRIGGER = 1
        else:
            TRIGGER = 0

        maxm = max(max(threshold_ema_slope_calc_01, threshold_ema_slope_calc_02), threshold_ema_slope_calc_03)

        if(i >= maxm):
            #down trend ema20 for threshold 01
            if(df["ema20"][i-threshold_ema_slope_calc_01] > df["ema20"][i] and TRIGGER == 1):
                print("SELL EMA 20 -> 01 at timestamp - ", df["Date"][i])
            #up trend ema20 for threshold 01
            elif(df["ema20"][i-threshold_ema_slope_calc_01] < df["ema20"][i] and TRIGGER == 1):
                print("BUY EMA 20 -> 01 at timestamp - ", df["Date"][i])
            
            #down trend ema20 for threshold 02
            if(df["ema20"][i-threshold_ema_slope_calc_02] > df["ema20"][i] and TRIGGER == 1):
                print("SELL EMA 20 -> 02 at timestamp - ", df["Date"][i])
            #up trend ema20 for threshold 02
            elif(df["ema20"][i-threshold_ema_slope_calc_02] < df["ema20"][i] and TRIGGER == 1):
                print("BUY EMA 20 -> 02 at timestamp - ", df["Date"][i])

            #down trend ema20 for threshold 03
            if(df["ema20"][i-threshold_ema_slope_calc_03] > df["ema20"][i] and TRIGGER == 1):
                print("SELL EMA 20 -> 03 at timestamp - ", df["Date"][i])
            #up trend ema20 for threshold 03
            elif(df["ema20"][i-threshold_ema_slope_calc_03] < df["ema20"][i] and TRIGGER == 1):
                print("BUY EMA 20 -> 03 at timestamp - ", df["Date"][i])

            #down trend ema100 for threshold 01
            if(df["ema100"][i-threshold_ema_slope_calc_01] > df["ema100"][i] and TRIGGER == 1):
                print("SELL EMA 100 -> 01 at timestamp - ", df["Date"][i])
            #up trend ema100 for threshold 01
            elif(df["ema100"][i-threshold_ema_slope_calc_01] < df["ema100"][i] and TRIGGER == 1):
                print("BUY EMA 100 -> 01 at timestamp - ", df["Date"][i])
            
            #down trend ema100 for threshold 02
            if(df["ema100"][i-threshold_ema_slope_calc_02] > df["ema100"][i] and TRIGGER == 1):
                print("SELL EMA 100 -> 02 at timestamp - ", df["Date"][i])
            #up trend ema100 for threshold 02
            elif(df["ema100"][i-threshold_ema_slope_calc_02] < df["ema100"][i] and TRIGGER == 1):
                print("BUY EMA 100 -> 02 at timestamp - ", df["Date"][i])

            #down trend ema100 for threshold 03
            if(df["ema100"][i-threshold_ema_slope_calc_03] > df["ema100"][i] and TRIGGER == 1):
                print("SELL EMA 100 -> 03 at timestamp - ", df["Date"][i])
            #up trend ema100 for threshold 03
            elif(df["ema100"][i-threshold_ema_slope_calc_03] < df["ema100"][i] and TRIGGER == 1):
                print("BUY EMA 100 -> 03 at timestamp - ", df["Date"][i])


            #down trend ema200 for threshold 01
            if(df["ema200"][i-threshold_ema_slope_calc_01] > df["ema200"][i] and TRIGGER == 1):
                print("SELL EMA 200 -> 01 at timestamp - ", df["Date"][i])
            #up trend ema200 for threshold 01
            elif(df["ema200"][i-threshold_ema_slope_calc_01] < df["ema200"][i] and TRIGGER == 1):
                print("BUY EMA 200 -> 01 at timestamp - ", df["Date"][i])
            
            #down trend ema200 for threshold 02
            if(df["ema200"][i-threshold_ema_slope_calc_02] > df["ema200"][i] and TRIGGER == 1):
                print("SELL EMA 200 -> 02 at timestamp - ", df["Date"][i])
            #up trend ema200 for threshold 02
            elif(df["ema200"][i-threshold_ema_slope_calc_02] < df["ema200"][i] and TRIGGER == 1):
                print("BUY EMA 200 -> 02 at timestamp - ", df["Date"][i])

            #down trend ema200 for threshold 03
            if(df["ema200"][i-threshold_ema_slope_calc_03] > df["ema200"][i] and TRIGGER == 1):
                print("SELL EMA 200 -> 03 at timestamp - ", df["Date"][i])
            #up trend ema200 for threshold 03
            elif(df["ema200"][i-threshold_ema_slope_calc_03] < df["ema200"][i] and TRIGGER == 1):
                print("BUY EMA 200 -> 03 at timestamp - ", df["Date"][i])
    # print("temp count: ",temp_count)




        # (2B)
        maxm2B = max(max(threshold_closevalue_ema_01, threshold_closevalue_ema_02), threshold_closevalue_ema_03)
        if(i >= maxm2B):
            if(df["ema20"][i-threshold_closevalue_ema_01] > df["ema20"][i] and TRIGGER == 1 and abs(df["Close"][i] - df["ema20"][i]) <= threshold_closevalue):
                print("SELL ON CLOSE VALUE ADJ EMA 20-> 01 at timestamp - ", df["Date"][i])
            elif(df["ema20"][i-threshold_closevalue_ema_01] < df["ema20"][i] and TRIGGER == 1 and abs(df["Close"][i] - df["ema20"][i]) <= threshold_closevalue):
                print("BUY ON CLOSE VALUE ADJ EMA 20-> 01 at timestamp - ", df["Date"][i])
            if(df["ema20"][i-threshold_closevalue_ema_02] > df["ema20"][i] and TRIGGER == 1 and abs(df["Close"][i] - df["ema20"][i]) <= threshold_closevalue):
                print("SELL ON CLOSE VALUE ADJ EMA 20-> 02 at timestamp - ", df["Date"][i])
            elif(df["ema20"][i-threshold_closevalue_ema_02] < df["ema20"][i] and TRIGGER == 1 and abs(df["Close"][i] - df["ema20"][i]) <= threshold_closevalue):
                print("BUY ON CLOSE VALUE ADJ EMA 20-> 02 at timestamp - ", df["Date"][i])
            if(df["ema20"][i-threshold_closevalue_ema_03] > df["ema20"][i] and TRIGGER == 1 and abs(df["Close"][i] - df["ema20"][i]) <= threshold_closevalue):
                print("SELL ON CLOSE VALUE ADJ EMA 20-> 03 at timestamp - ", df["Date"][i])
            elif(df["ema20"][i-threshold_closevalue_ema_03] < df["ema20"][i] and TRIGGER == 1 and abs(df["Close"][i] - df["ema20"][i]) <= threshold_closevalue):
                print("BUY ON CLOSE VALUE ADJ EMA 20-> 03 at timestamp - ", df["Date"][i])

            
            if(df["ema100"][i-threshold_closevalue_ema_01] > df["ema100"][i] and TRIGGER == 1 and abs(df["Close"][i] - df["ema100"][i]) <= threshold_closevalue):
                print("SELL ON CLOSE VALUE ADJ EMA 100-> 01 at timestamp - ", df["Date"][i])
            elif(df["ema100"][i-threshold_closevalue_ema_01] < df["ema100"][i] and TRIGGER == 1 and abs(df["Close"][i] - df["ema100"][i]) <= threshold_closevalue):
                print("BUY ON CLOSE VALUE ADJ EMA 100-> 01 at timestamp - ", df["Date"][i])
            if(df["ema100"][i-threshold_closevalue_ema_02] > df["ema100"][i] and TRIGGER == 1 and abs(df["Close"][i] - df["ema100"][i]) <= threshold_closevalue):
                print("SELL ON CLOSE VALUE ADJ EMA 100-> 02 at timestamp - ", df["Date"][i])
            elif(df["ema100"][i-threshold_closevalue_ema_02] < df["ema100"][i] and TRIGGER == 1 and abs(df["Close"][i] - df["ema100"][i]) <= threshold_closevalue):
                print("BUY ON CLOSE VALUE ADJ EMA 100-> 02 at timestamp - ", df["Date"][i])
            if(df["ema100"][i-threshold_closevalue_ema_03] > df["ema100"][i] and TRIGGER == 1 and abs(df["Close"][i] - df["ema100"][i]) <= threshold_closevalue):
                print("SELL ON CLOSE VALUE ADJ EMA 100-> 03 at timestamp - ", df["Date"][i])
            elif(df["ema100"][i-threshold_closevalue_ema_03] < df["ema100"][i] and TRIGGER == 1 and abs(df["Close"][i] - df["ema100"][i]) <= threshold_closevalue):
                print("BUY ON CLOSE VALUE ADJ EMA 100-> 03 at timestamp - ", df["Date"][i])


            if(df["ema200"][i-threshold_closevalue_ema_01] > df["ema200"][i] and TRIGGER == 1 and abs(df["Close"][i] - df["ema200"][i]) <= threshold_closevalue):
                print("SELL ON CLOSE VALUE ADJ EMA 200-> 01 at timestamp - ", df["Date"][i])
            elif(df["ema200"][i-threshold_closevalue_ema_01] < df["ema200"][i] and TRIGGER == 1 and abs(df["Close"][i] - df["ema200"][i]) <= threshold_closevalue):
                print("BUY ON CLOSE VALUE ADJ EMA 200-> 01 at timestamp - ", df["Date"][i])
            if(df["ema200"][i-threshold_closevalue_ema_02] > df["ema200"][i] and TRIGGER == 1 and abs(df["Close"][i] - df["ema200"][i]) <= threshold_closevalue):
                print("SELL ON CLOSE VALUE ADJ EMA 200-> 02 at timestamp - ", df["Date"][i])
            elif(df["ema200"][i-threshold_closevalue_ema_02] < df["ema200"][i] and TRIGGER == 1 and abs(df["Close"][i] - df["ema200"][i]) <= threshold_closevalue):
                print("BUY ON CLOSE VALUE ADJ EMA 200-> 02 at timestamp - ", df["Date"][i])
            if(df["ema200"][i-threshold_closevalue_ema_03] > df["ema200"][i] and TRIGGER == 1 and abs(df["Close"][i] - df["ema200"][i]) <= threshold_closevalue):
                print("SELL ON CLOSE VALUE ADJ EMA 200-> 03 at timestamp - ", df["Date"][i])
            elif(df["ema200"][i-threshold_closevalue_ema_03] < df["ema200"][i] and TRIGGER == 1 and abs(df["Close"][i] - df["ema200"][i]) <= threshold_closevalue):
                print("BUY ON CLOSE VALUE ADJ EMA 200-> 03 at timestamp - ", df["Date"][i])

            
            

    # print(len(ema_20_100_flag))
    # print(len(df))

    df["ema_20_100_flag"] = ema_20_100_flag
    df["ema_100_200_flag"] = ema_100_200_flag
    df["ema_20_200_flag"] = ema_20_200_flag
    df["ema100_BBH_flag"] = ema100_BBH_flag
    df["ema200_BBH_flag"] = ema200_BBH_flag
    df["ema100_BBL_flag"] = ema100_BBL_flag
    df["ema200_BBL_flag"] = ema200_BBL_flag

    df["flag_close_100ema"] = flag_close_100ema
    df["flag_close_200ema"] = flag_close_200ema
    df["flag_close_BBU"] = flag_close_BBU
    df["flag_close_BBL"] = flag_close_BBL

    print(minm_close_ema100)
    print(minm_close_ema200)
    print(minm_close_bb_bbh)
    print(minm_close_bb_bbl)

    df.to_csv('out.csv')

    
