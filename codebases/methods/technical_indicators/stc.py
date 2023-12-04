from ta.trend import STCIndicator

def STC(dataframe):
    stc = STCIndicator(dataframe["close"], window_slow=50, window_fast=26, cycle=12).stc()
    dataframe["stc"] = stc
    return dataframe