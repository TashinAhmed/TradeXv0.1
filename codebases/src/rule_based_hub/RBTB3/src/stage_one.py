''' 
This file is used to calculate the profit/loss of the strategy in basis of EMA intersections 
(currently EMA100 = 20 and EMA200 = 30 while calculating up and down trend and a tracing intersection till 10 timestamps)
'''
import time 

from config import *
from indicators import *
from proc_indicators_intersection import *
from debugger import *


# def buyCondition():
#     pass

# def sellCondition(operation_flag, pips, close_val, pips_counter, current_balance, counter):
#     counter += 1
#     if operation_flag == 0 and pips > 0:
#         pip_value = close_val * pips_counter
#         current_balance = current_balance + pip_value
#         pips -= pips_counter
#         print(f"SELL: {current_balance}, pips: {pips}, bought: {pip_value}")
#         operation_flag = 1

def emaInterestionTrend(df, len_df, current_balance, trace, trace2, counter, pips, keeper_balance, HIGHEST_TRACE_LIMIT):

    signalBuy = []
    signalSell = []

    signalBuy.append(np.nan)
    signalSell.append(np.nan)

    for i in range(1, len_df):
        
        # time.sleep(0.4)
        operation_flag = 0 # to maintain single operation per iteration
        HOLD_TRIGGER = 0

        # ema 100 and 200 intersection trigger
        if(df["ema_100_200_diff"][i] > 0):
            ema_100_200_flag.append(1)
        elif(df["ema_100_200_diff"][i] < 0):
            ema_100_200_flag.append(0)
        elif(df["ema_100_200_diff"][i] == 0):
            ema_100_200_flag.append(ema_100_200_flag[i-1])

        # ema 100 and 200 trigger based decision
        if(ema_100_200_flag[i] != ema_100_200_flag[i-1]):
            ema_100_200_trigger = 1
            trace = i
            # print(f"100X200 trigger at: {i}")
        else:
            ema_100_200_trigger = 0

        # bbh and ema 100 intersection trigger
        if(df["ema100_BBH_diff"][i] > 0):
            ema100_BBH_flag.append(1)
        elif(df["ema100_BBH_diff"][i] < 0):
            ema100_BBH_flag.append(0)
        elif(df["ema100_BBH_diff"][i] == 0):
            ema100_BBH_flag.append(ema100_BBH_flag[i-1])

        # bbh and ema 100 trigger based decision
        if(ema100_BBH_flag[i] != ema100_BBH_flag[i-1]):
            ema100_BBH_trigger = 1
            trace2 = i
            # print(f"100XBBH trigger at: {i}")
        else:
            ema100_BBH_trigger = 0
        
        # bbl and ema 100 intersection trigger
        # bbh and ema 200 intersection trigger
        # bbl and ema 200 intersection trigger

        


        if(ema_100_200_trigger == 1 and i >= threshold_slope_ema): 
            
            #down trend ema100 for threshold 03
            if(df["ema100"][i-threshold_slope_ema] > df["ema100"][i] and abs(df["Close"][i] - df["ema100"][i]) <= threshold_closevalue):
                # sell 
                # debugger(threshold_slope_ema)
                pips_current = 4
                if (pips - pips_current < 0):
                    pips_current = pips
                counter += 1
                if operation_flag == 0 and pips > 0:
                    pip_value = df['Close'][i] * pips_current
                    current_balance = current_balance + pip_value
                    pips -= pips_current
                    if(current_balance < initial_balance):
                        pip_value = df['Close'][i] * pips
                        current_balance = current_balance + pip_value
                        pips -= pips
                    print(f"SELL: {current_balance}, USD: {pips}, bought: {pip_value}, datetime: {df['Date'][i]}")
                    signalSell.append(df['Close'][i])
                    signalBuy.append(np.nan)
                    HOLD_TRIGGER = 1
                    operation_flag = 1


            #up trend ema100 for threshold 03
            elif(df["ema100"][i-threshold_slope_ema] < df["ema100"][i] and abs(df["Close"][i] - df["ema100"][i]) <= threshold_closevalue):
                counter += 1
                # buy 
                pips_current = 4
                if operation_flag == 0:
                    pip_value = df['Close'][i] * pips_current
                    temp_balance = current_balance - pip_value
                    if(temp_balance > keeper_balance):
                        current_balance = current_balance - pip_value
                        pips += pips_current
                        print(f"BUY: {current_balance}, USD: {pips}, datetime: {df['Date'][i]}")
                        signalBuy.append(df['Close'][i])
                        signalSell.append(np.nan)
                        HOLD_TRIGGER = 1
                    else:
                        print(f"INSUFFICIENT BALANCE, datetime: {df['Date'][i]}")
                    operation_flag = 1


            #down trend ema200 for threshold 01
            if(df["ema200"][i-threshold_slope_ema] > df["ema200"][i] and abs(df["Close"][i] - df["ema200"][i]) <= threshold_closevalue):
                # sell 
                pips_current = 6
                if (pips - pips_current < 0):
                    pips_current = pips
                counter += 1
                if operation_flag == 0 and pips > 0:
                    pip_value = df['Close'][i] * pips_current
                    current_balance = current_balance + pip_value
                    pips -= pips_current
                    if(current_balance < initial_balance):
                        pip_value = df['Close'][i] * pips
                        current_balance = current_balance + pip_value
                        pips -= pips
                    print(f"SELL: {current_balance}, USD: {pips}, bought: {pip_value}, datetime: {df['Date'][i]}")
                    signalSell.append(df['Close'][i])
                    signalBuy.append(np.nan)
                    HOLD_TRIGGER = 1
                    operation_flag = 1
            
            #up trend ema200 for threshold 01
            elif(df["ema200"][i-threshold_slope_ema] < df["ema200"][i] and abs(df["Close"][i] - df["ema200"][i]) <= threshold_closevalue):
                counter += 1
                # buy 
                pips_current = 6
                if operation_flag == 0:
                    pip_value = df['Close'][i] * pips_current
                    temp_balance = current_balance - pip_value
                    if(temp_balance > keeper_balance):
                        current_balance = current_balance - pip_value
                        pips += pips_current
                        print(f"BUY: {current_balance}, USD: {pips}, bought: {pip_value}, datetime: {df['Date'][i]}")
                        signalBuy.append(df['Close'][i])
                        signalSell.append(np.nan)
                        HOLD_TRIGGER = 1
                    else:
                        print(f"INSUFFICIENT BALANCE, datetime: {df['Date'][i]}")
                    operation_flag = 1



            
        
        if(ema100_BBH_trigger == 0 and i >= threshold_lookback_ema100_bbh): 
            
            if(df["BBH"][i-threshold_slope_ema] < df["BBH"][i] and abs(df["Close"][i] - df["BBH"][i]) <= threshold_closevalue):
                # sell
                pips_current = 2
                # debugger(pips_current)
                if (pips - pips_current < 0):
                    pips_current = pips
                counter += 1
                if operation_flag == 0 and pips > 0:
                    pip_value = df['Close'][i] * pips_current
                    current_balance = current_balance + pip_value
                    pips -= pips_current
                    if(current_balance < initial_balance):
                        pip_value = df['Close'][i] * pips
                        current_balance = current_balance + pip_value
                        pips -= pips
                    print(f"SELL: {current_balance}, USD: {pips}, bought: {pip_value}, datetime: {df['Date'][i]}")
                    signalSell.append(df['Close'][i])
                    signalBuy.append(np.nan)
                    HOLD_TRIGGER = 1
                    operation_flag = 1
            elif(df["BBH"][i-threshold_slope_ema] > df["BBH"][i] and abs(df["Close"][i] - df["BBH"][i]) <= threshold_closevalue):
                counter += 1
                # buy 
                pips_current = 2
                if operation_flag == 0:
                    pip_value = df['Close'][i] * pips_current
                    temp_balance = current_balance - pip_value
                    if(temp_balance > keeper_balance):
                        current_balance = current_balance - pip_value
                        pips += pips_current
                        print(f"BUY: {current_balance}, USD: {pips}, bought: {pip_value}, datetime: {df['Date'][i]}")
                        signalBuy.append(df['Close'][i])
                        signalSell.append(np.nan)
                        HOLD_TRIGGER = 1
                    else:
                        print(f"INSUFFICIENT BALANCE, datetime: {df['Date'][i]}")
                    operation_flag = 1
        
        # no buy/sell trigger
        if HOLD_TRIGGER == 0:
            # print(f"HOLD, datetime: {df['Date'][i]}")
            signalSell.append(np.nan)
            signalBuy.append(np.nan)

    df['Buy'] = signalBuy
    df['Sell'] = signalSell
    print("counter from inside: ", counter)
    