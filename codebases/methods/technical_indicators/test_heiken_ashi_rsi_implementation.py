# https://medium.com/swlh/heiken-ashi-trading-the-full-guide-in-python-8abb951637f


def heiken_ashi(Data, opening, high, low, close, where):
    # Heiken-Ashi Open
    try:
        for i in range(len(Data)):
            Data[i, where] = (Data[i - 1, opening] + Data[i - 1, close]) / 2
    except:
        pass
    # Heiken-Ashi Close
    for i in range(len(Data)):
        Data[i, where + 3] = (Data[i, opening] + Data[i, high] + Data[i, low] + Data[i, close]) / 4
    # Heiken-Ashi High
    for i in range(len(Data)):    
        Data[i, where + 1] = max(Data[i, where], Data[i, where + 3], Data[i, high])
    # Heiken-Ashi Low    
    for i in range(len(Data)):    
        Data[i, where + 2] = min(Data[i, where], Data[i, where + 3], Data[i, low])      
    return Data
# To be used on an OHLC array with a few columns to spare
my_ohlc_array = heiken_ashi(my_ohlc_array, 0, 1, 2, 3, 4)
# The numbers signify in order: Open, High, Low, Close, then the column indexed at 4 is where 
# the first new Heiken OHLC data will be populated (Meaning that the columns 4, 5, 6, and 7 will 
# have a brand new OHLC data)


def signal(Data, heiken_close, heiken_open, buy, sell):
    for i in range(len(Data)):
        if Data[i, heiken_close] > Data[i, heiken_open] and Data[i - 1, heiken_close] < Data[i - 1, heiken_open]:
            Data[i, buy] = 1
        if Data[i, heiken_close] < Data[i, heiken_open] and Data[i - 1, heiken_close] > Data[i - 1, heiken_open]:
            Data[i, sell] = -1
# The variable heiken_close refers to the Heiken closing candle
# The variable heiken_open refers to the Heiken opening candle