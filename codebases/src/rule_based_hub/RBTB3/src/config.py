if(input("Press 1 to give manual threshold as input or enter to proceed with default values: ") == "1"):
    threshold_closeprice_with_indicators = float(input("Enter threshold difference for close price - indicators: "))
    threshold_slope_ema = int(input("Enter threshold for EMA slope calc: "))
    threshold_closevalue = float(input("Enter threshold for close value: "))
    threshold_closevalue_ema = float(input("Enter threshold for close value EMA distance calc: "))    
    intial_balance = float(input("Enter initial balance: "))

else:
    # threshold_closeprice_with_indicators = 2.5
    threshold_slope_ema = 5
    threshold_lookback_ema100_bbh = 20
    threshold_closevalue = .5
    # threshold_closevalue_ema = 2
    initial_balance = current_balance = 10000.0


# DATA_PATH = "../data/USDJPY_historical_data.csv"
DATA_PATH = "../data/reverse_data_3.csv"

trace = 0                   # trace to track after an interesction between two EMA
trace2 = 0                  # trace to track after an interesction between EMA100 and BBH
counter = 0                 # counter for how many buy and sell took place
pips = 0                    # pips availability with the user
keeper_balance = 0.1        # lowest balance to keep by the user; less than this balance no buy will be triggered
HIGHEST_TRACE_LIMIT = 10    # limit for the trace to be considered as a buy/sell
HIGHEST_TRACE_LIMIT2 = 20   # limit for the trace to be considered as a buy/sell 100BBH


ema_20_100_diff = []    # differences of EMA 20 and 200
ema_100_200_diff = []   # differences of EMA 100 and 200   
ema_20_200_diff = []    # differences of EMA 100 and 200
ema100_BBH_diff = []    # differences of EMA 100 and BBH
ema200_BBH_diff = []    # differences of EMA 200 and BBH
ema100_BBL_diff = []    # differences of EMA 100 and BBL
ema200_BBL_diff = []    # differences of EMA 200 and BBL



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
minm_close_BBH = 0
minm_close_BBL = 0